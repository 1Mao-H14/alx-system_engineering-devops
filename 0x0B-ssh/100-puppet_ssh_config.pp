#!/usr/bin/env bash
# ust as in the previous configuration file task, we’d like you to set up your client SSH configuration file
#  so that you can connect to a server without typing a password.
file {'/etc/ssh/shh_config':
	ensure  => 'present',
}

file_line {'Turn off passwd auth':
	path    => '/etc/ssh/ssh_config',
	line    => 'PasswordAuthentication no',
	match   => 'PasswordAuthentication yes',
	replace => 'true',
	
}
file_line {'Declare identity file':
	path    => '/etc/ssh/ssh_config',
	line    => 'IdentityFile ~/.ssh/school',
	match   => '^IdentityFile',
	ensure  => 'present',
}
