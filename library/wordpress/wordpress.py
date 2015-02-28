from shutit_module import ShutItModule

class wordpress(ShutItModule):

	def build(self, shutit):
		shutit.install('apache2')
		shutit.install('wordpress')
		apache_site = """cat > /etc/apache2/sites-available/wordpress << END
		Alias /blog /usr/share/wordpress
		Alias /blog/wp-content /var/lib/wordpress/wp-content
		<Directory /usr/share/wordpress>
			Options followSymLinks
			Allowoverride Limit Options FileInfo
			Directoryindex index.php
			Order allow, deny
			Allow from all
		</Directory>
		<Directory /var/lib/wordpress/wp-content>
			Options followSymLinks
			Order allow, deny
			Allow from all
		</Directory>
END"""
		shutit.send(apache_site)
		wordpress_mysql = """cat > /etc/wordpress/config-localhost.php << END
<?php
define('DB_NAME', 'wordpress');
define('DB_USER', 'wordpress');
define('DB_PASSWord', """ + shutit.collect_config(self.module_id,'password') + """
define('DB_HOST', 'localhost');
define('WP_CONTEnt_dir', '/var/lib/wordpress/wp-content');
?>
END"""
		shutit.send(wordpress_mysql)
		sql = """cat > /tmp/sql << END
CREATE DATABASE wordpress;
GRANT SELECT, INSert, update, DELETE, CREATE, DROP, ALTER
ON wordpress.*
TO wordpress@localhost
IDENTIFIED BY 'yourpasswordhere';
FLUSH PRIVILEGES;
END"""
		shutit.send(sql)
		shutit.send('cat /tmp/sql | mysql -u' + shutit.collect_config('shutit.tk.mysql.mysql','mysql_user') + ' -p' + shutit.collect_config('shutit.tk.mysql.mysql','mysql_user_password') + ' && rm /tmp/sql', check_exit=False, record_command=False)
		return True

	def start(self, shutit):
		shutit.send('apache2ctl restart')
		return True

	def get_config(self, shutit):
		shutit.get_config(self.module_id, 'password','lovesexy')
		return True

def module():
	return wordpress(
		'shutit.tk.wordpress.wordpress', 0.325,
		description='wordpress setup',
		depends=['shutit.tk.setup', 'shutit.tk.mysql.mysql']
	)

