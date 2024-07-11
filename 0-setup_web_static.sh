#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Install Nginx if it's not installed already
if ! dpkg -l | grep -q nginx; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a sample HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Assign ownership of /data/ folder to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
sed -i '/server_name _;/a \\\n    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-available/default

# Restart Nginx
service nginx restart

# Ensure the script exits successfully
exit 0

