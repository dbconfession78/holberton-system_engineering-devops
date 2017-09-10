# turn on display_errors in /etc/php5/apach2/php.ini
exec { 'fix typo,  extra p in php extension':
  command => 'sed  -i "s@.phpp@.php@" /var/www/html/wp-settings.php',
  path    => ['/bin','/sbin','usr/bin','usr/sbin']
}

# to use this, first run 'puppet module install puppetlabs-stdlib --version 4.19.0'
# file_line { 'fix typo,  extra p in php extension':
#  path  => '/var/www/html/wp-settings.php',
#  line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
#  match => 'require_once\( ABSPATH . WPINC . \'/class-wp-locale.phpp\' \);'
#}
