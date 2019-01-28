# Steps to run the hello-world dag with LOCAL EXECUTOR 

1.  start postgresql server 
##### $ systemctl start postgresql

2. 	run the script
##### $ python AIRFLOW_HOME/dags/hello_world_dag.py 

3. 	start airflow webserver
##### $ airflow webserver -p 8080

4. 	start airflow scheduler
##### $ airflow scheduler

5. 	go to airflow webserver  
##### http://HOST:8080

6. 	turn on the dag
7.	trigger the dag
