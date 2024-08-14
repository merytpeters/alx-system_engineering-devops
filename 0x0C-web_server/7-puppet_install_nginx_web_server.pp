# Puppet manifest to install and configure Nginx

# Ensure Nginx package is installed
package { 'nginx':
  ensure  => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Ensure the default Nginx config is in place
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => '
server {
    listen 80;

    # Root configuration
    location / {
        # Return "Hello World!" at the root
        default_type text/html;
        return 200 "Hello World!\n";
    }

    # Redirect /redirect_me to root with a 301 Moved Permanently
    location /redirect_me {
        return 301 /;
    }
}
',
  notify  => Service['nginx'],
}

# Ensure the Nginx configuration is properly linked
file { 'etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}
