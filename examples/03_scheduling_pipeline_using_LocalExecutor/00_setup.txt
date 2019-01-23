In Airflow terminology, an "Executor" is the component responsible for running your task. The LocalExecutor does this by spawning threads on the computer Airflow runs on and lets the thread execute the task.

Under the pseudo-distributed mode with a local executor, the local workers pick up and run jobs locally via multiprocessing. If you have only a moderate amount of scheduled jobs, this could be the right choice.

### Prerequisites
1. You need to install some sub-packages: 
	i) for PostgreSQL DBs
		# pip install airflow[postgres]

2. By default, Airflow uses SQLite as database. You Need to install PostgreSQL or MySQL to support parallelism using any executor other than sequential. I am using PostgreSQL for this. If you have not already installed it, follow 01_PostgreSQL_installation guide, otherwise skip  the next step.

3. Update the configuration in AIRFLOW_HOME/airflow.cfg, follow 02_update_airflow.cfg
   