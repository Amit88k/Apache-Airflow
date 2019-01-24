import logging
import os
import sys

from airflow import DAG
from airflow.operators import PythonOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime


args = {
  'owner': 'airflow',
  'start_date': datetime(2019, 1, 7),
  'provide_context': True
}

dag = DAG(
  'scheduling_spark_using_airflow',
  start_date = datetime(2019, 1, 7),
  schedule_interval = '@once',
  default_args = args
)

#os.environ['SPARK_HOME'] = '/opt/mapr/spark/saprk-2.1.0'
#sys.path.append(os.path.join(os.environ['SPARK_HOME'], 'bin'))

#export SPARK_HOME,
#export PATH="$SPARK_HOME/bin/:$PATH"

spark_task= BashOperator(
    task_id='task_spark_wordcount',
    bash_command='spark-submit  --class {{ params.class }} {{ params.jar }} {{ params.file }}',
    params={'class': 'com.nagarro.practice.sparkhelloworld.SparkHelloWorld', 'jar': 'file:///root/airflow/SparkWordCount-0.0.1-SNAPSHOT.jar', 'file': 'file:///root/airflow/sales.csv'},
  #  bash_command = 'echo $SPARK_HOME', 
   dag=dag
)

templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

t3 = BashOperator(
    task_id='task_templated',
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag)

t3.set_upstream(spark_task)
