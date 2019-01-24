In AIRFLOW_HOME/airflow.cfg 

1. comment out 
	executor=SequenceExecutor
	
2. add 
	 executor=LocalExecutor
	 
3. reset sql_alchemy_conn property to:
	 sql_alchemy_conn = postgresql+psycopg2://postgres:@127.0.0.1:5432/sample_database
	 
### above connection for project database:
	A connection type of Postgres.
	A connection identifier of users (postgres).
	A host string of 127.0.0.1.
	PostgreSQL Port - 5432
	A schema string (database name) of sample_database.
	A login of postgres (default).
	 
4. Restart airflow db: 
	 airflow initdb
	 
Now, your set up is ready. 

Now you can run any of the dags, your dags will using local executors.

NOTE: PORT 5432 for postgresql is set in  var/lib/pgsql/data/postgresql.conf.


