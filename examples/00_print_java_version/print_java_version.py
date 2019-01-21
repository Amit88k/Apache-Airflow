
### An Airflow pipeline is just a Python script that happens to define an Airflow DAG object.

from airflow import DAG   # The DAG object; we'll need this to instantiate a DAG
from airflow.operators import BashOperator  # Operators; we need this to operate!
from datetime import datetime
import os
import sys

args = {
  'owner': 'airflow'
  , 'start_date': datetime(2019, 1, 7)
  , 'provide_context': True
}
d = datetime(2019, 1, 7)


### Instantiate a DAG - We’ll need a DAG object to nest our tasks into. Here we pass a string that defines the dag_id (print_java_version), which     ### serves as a unique identifier for your DAG. We also pass the default argument dictionary that we just defined and define a schedule_interval to   ### just once for the DAG.  
dag = DAG('print_java_version', start_date = d, schedule_interval = '@once', default_args = args)


### Tasks - Tasks are generated when instantiating operator objects. An object instantiated from an operator is called a constructor. The first argument task_id acts as a unique identifier for the task. We can have multiple tasks.
t_main = BashOperator(
  task_id = 'usgs_fetch'
  , dag = dag
  , bash_command = 'java -version'
  #params = {'class': 'FetchJSON', 'path': 'jars/kafkaUSGS.jar'}
  )


### Running the script
### Let’s assume we’re saving the code from the previous step in
### print_java_version.py in the DAGs folder referenced in your airflow.cfg.
### The default location for your DAGs is ~/airflow/dags.

# run command - python ~/airflow/dags/print_java_version.py 
# or
# run command - python path/to/airflow/dags/print_java_version.py

### start airflow webserver - 
# run command - airflow webserver -p 8080

### start airflow scheduler -
# run command - airflow scheduler

### Go to web UI at http://host_ip:8080
### You will get the name of dag in the dag list on UI as shown in image1.
### start the dag as shown in image2.
### trigger the dag as shown in image3.
### Refresh 
### you can find the logs as shown in image4, image5, image5 and image7.