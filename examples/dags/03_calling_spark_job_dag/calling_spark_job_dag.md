For a scheduling a spark job using Airflow, a dag named 'scheduling_spark_using_airflow is created which contains python script -  calling_spark_job_dag.py. Dag is scheduled to run once. 

Dag contains two tasks - task_spark_wordcount and task_templeted. Task task_spark_wordcount runs a bash command to submit spark job. SparkWordCOunt-0.0.1-SNAPSHOT.jar which reads data from sales.csv and produces results in output directory. Three arguments are passed to the bash command fully qualified class name, the path of the jar (which, I have kept in ~/airflow) and the fully qualified name of the file to process  (which, I have kept in ~/airflow).

You verify output directory using the command : 
#### hadoop fs -ls /user/root/output
 
#### Note - Task can show an error, if the directory will already be present at that location. Please delete the directory every time, before you trigger the dag. 

Another task is task_templeted which is a python code and it prints today's and 7 days later - "date stamps" and the parameter passed in a loop for 5 times.

