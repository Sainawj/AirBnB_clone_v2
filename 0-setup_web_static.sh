#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Update package lists
apt-get update

# Install Nginx
apt-get install -y nginx

# Create directories for the test release and shared data
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a test HTML file with provided HTML structure
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link to the test release
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change ownership of the /data/ directory to the ubuntu user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx to serve content from the new directories
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
service nginx restart
