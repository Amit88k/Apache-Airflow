In AIRFLOW_HOME/airflow.cfg 

1. comment out 
	executor=SequenceExecutor
	
2. add 
	 executor=LocalExecutor
	 
3. reset sql_alchemy_conn property to:
	 sql_alchemy_conn = postgresql+psycopg2://postgres:@127.0.0.1:5432/sample_database
	 
4. Restart airflow db: 
	 airflow initdb
	 
Now, your set up is ready. 

NOTE: PORT 5432 for postgresql is set in  var/lib/pgsql/data/postgresql.conf.


