# script to automate and fix Apache 500 error
file { '/var/www/html/wp-settings.php':
  ensure => present
}
-> exec { 'replace':
  command => "sed -i 's/.phpp/.php/' var/www/html/wp-settings.php",
  path    => '/bin'
}
