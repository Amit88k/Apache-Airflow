### TODO:	
	1. explaination about the pipeline.
 	2. provide [mapr-variant-jar] [cloudera-variant-jar] [spark-code]
	3. start the airflow webserver
	4. start the airflow scheduler
	5. submit or compile the python file 
	6. start from the webserver
	
1. Start the PostgreSQL Server 
	##### sudo systemctl restart postgresql
	
2. Initialize Airflow DB, if you have not done already after modifications in configurations
	##### airflow initdb
	
3. Submit the dag you want to run
	##### python [/path/to/dags/directory/dag_you_want_to_run]
	e.g.  python ~/airflow/dags/tutorial.py

3. Start webserver 
	##### airflow webserver -p 8080
	
4. Start scheduler
	##### airflow scheduler

	