import sys

from airflow import DAG
from airflow.operators import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

from airflow.utils.trigger_rule import TriggerRule

default_args = {
	'owner': 'airflow',
	'depends_on_past': False # always reschedule DAG task everyday in ignorance of previous day's state (whether succeed or fail) of DAG task).
	'start_date': datetime(2019, 1, 26),
	'retries': 0,
	'retry_delay': timedelta(minute=1),
}

dag = DAG(
	'hello_world_v1',
	start_date = datetime(2019, 1, 26),
	schedule_interval='@once',
	default_args = default_args
)

# t1, t2, and t3 are examples of tasks created by instantiating operators

t1 = BashOperator(
	task_id='task_1',
	bash_command='echo "Hello World! from Task_1 ',
	dag=dag
)

t2 = BashOperator(
	task_id='task_2',
	bash_command='echo "Hello World! from Task_2" ',
	dag=dag
)

t3 = BashOperator(
	task_id='task_3',
	bash_command='echo "Hello World! from Task_3" ',
	dag=dag
)

t1 >> t3 << t2 