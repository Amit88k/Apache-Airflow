### Exploring how PostgreSQL is benefiting here. 

###After running the sample sample pipeline,
1. go to PostgreSQL cli 
	$ psql -U postgres
	
2. list all the databases 
	# \l
	
3. connect to the database which we have set in the AIRFLOW_HOME/airflow.cfg 
	# \c sample_database
	
4. verify the tables created
	# \d
	
In postgres_images directory : 
5. localExecutor-airflow-cfg.png contains the information about the modification in AIRFLOW_HOME/airflow.cfg i.e. information about the executor and sql_alchemy_conn.

6. all_tables.png image shows all the tables and sequences that got created in PostgreSQL after successful completion of the pipeline scheduled in Airflow.

7. dag_table_structure.png image tells about the columns, their types and about primary key.

8. dag_table.png image contains the information about all the dags, their states i.e. is_paused, is_subdag, is_active, last_scheduler_run etc.

9. job_table.png contains the information about all the jobs such as dag_id, state, job_type, start_date, executor_class, primary key, etc.

10. a table for failed tasks also got created named as task_fail. task_fail_table.png contains the information about the failed tasks along with its structure.

11. a table is also got created for the logs which is shown in log_table.png image it contains the information such as dag_id, task_is, event (status of the task), etc.
