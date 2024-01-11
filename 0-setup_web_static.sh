#!/usr/bin/env bash
#Set up web servers for the deployment of web_static

#Install Nginx if it not already installed
sudo apt update
sudo apt install nginx -y

#Create default nginx folder for the pages.
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

#Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
#If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo rm /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Give ownership of the /data/ folder to the ubuntu user AND group ( should be recursive).
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static.
sudo sed -i "s/server_name _;/&\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t}\n/" /etc/nginx/sites-enabled/default

#Restart nginx server
sudo service nginx restart
