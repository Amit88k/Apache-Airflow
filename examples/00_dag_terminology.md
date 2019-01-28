Before writing a dag, one should know the following concepts.

## 1. Default Arguments
A dictionary of default_arguments can be passed to a DAG, to overwrite default values of the DAG arguments. It can be applied to any of its operators. This is a way to apply common parameters to many operators without having to specify for each DAG.
#### example
	default_args = {
    'start_date': datetime(2019, 1, 26),
    'owner': 'Airflow'
	}

	dag = DAG('example_dag', default_args=default_args)
	op = DummyOperator(task_id='dummy', dag=dag)
	print(op.owner) # Airflow
	
Some of the arguments, to be taken care of : 
#### start date argument
