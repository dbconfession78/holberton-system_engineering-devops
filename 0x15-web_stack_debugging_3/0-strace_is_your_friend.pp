# fix typo extension .phpp typo on line 137 by removeing extra 'p'
file_line { 'fix: remove trailing \'p\'in extension \'.phpp.\' );':
  path  => '/var/www/html/wp-settings.php',
  line  => 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );',
  match => 'require_once\( ABSPATH . WPINC . \'/class-wp-locale.phpp\' \);'
}
