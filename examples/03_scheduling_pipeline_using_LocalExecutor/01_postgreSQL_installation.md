### installing PostgreSQL on centos

1. Install the postgresql-server and the contrib package, which provide you some additional utilities and functionalities:
	$ sudo yum install postgresql-server postgresql-contrib
	
2. Create a new PostgreSQL database cluster:
	$ sudo postgresql-setup initdb
	
NOTE: By default, PostgreSQL doesn't allow password authentication. We can change that by editing its host-based authentication (HBA) configurations.

3. Open the HBA configuration file and change the method of all the hosts from ident to either trust or md5.
	Upon installation, Postgres is set up to use "ident" authentication, meaning that it associates Postgres roles with a matching Unix/Linux system account. If a Postgres role exits, it can be signed by logging into the associated Linux system account.

NOTE: also uncomment, configurations for user - postgres, if commented, by default.

NOTE: You can use the following command to get the location of config file: 
	$ ps auxw | grep postgres | grep -- -D

4. Save and exit. PostgreSQL is now configured to allow password authentication. 

5. Now start PostgreSQL server:
	$ sudo systemctl restart postgresql

6. The installation procedure created a user account called postgres that is associated with the default Postgres role. In order to use PostgreSQL, we'll need to log into that account. You can do that by the command : 
	$ sudo -i -u postgres
	
7. You can get a PostgreSQL prompt immediately by typing :
	$ psql
		You will be auto logged in and will be able to interact with the database management system right away.

	OR 
	
	if the above command throws an error, you can do :
	$ psql -U postgres
	
8. Now, either you can set PostgreSQL to start on booting as : 
	$ sudo systemctl enable postgresql
	
	OR 
	
	follow the following step every time :
		1. start PostgreSQL-server, using following command :
			$ systemctl restart postgresql
			
##### TODO: 
1. We will use sample_database in out all sample programs. Update document with database creation steps  

	
	
	
	

