# Increases  ++ THE of traffic AMOUNT OF NGINX server

# depqnqge nginxreauests
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# rreloqding nginxx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
