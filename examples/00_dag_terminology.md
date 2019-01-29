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
	
Some of the parameters of default arguments, should be taken care of : 

#### task_id (String)
a unique, meaningful id for the task.

#### retries (int)
the number of retries that should be performed before failing the task.

#### retry_delay (timedelta)
delay between retries.

#### max_retry_delay (timedelta)
maximum delay interval between retries.  

#### start_date
the start_date for the task, determines the execution_date for the first task instance. 
 
#### execution date (Conceptual)
Airflow sets execution_date based on the left bound of the schedule period it is covering, not based on when it fires (which would be the right bound of the period). When running a schedule='@hourly' task for instance, a task will fire every hour. The task that fires at 2pm will have an execution_date of 1pm because it assumes that you are processing the 1pm to 2pm time window at 2pm. Similarly, if you run a daily job, the run with execution_date of 2019-01-29 would trigger soon after midnight on 2019-01-30.

This left bound lebelling makes a lot of sense when thinking in terms of ETL and differential loads, but gets confuing when thinking in terms of a simple cron-like scheduler.

NOTE - Airflow simply looks at the latest execution_date and adds the scheduler_interval to determine the next execution_date. It is also very important to note that different task's dependencies need to line up in time. If a task A depends on task B and their start_date are offset in a way that their execution_date don't line up, A's dependencies will never be met.

#### end_date (datetime)
date beyond which scheduler won't go.

#### task_concurrency (int) 
the number of Task Instances to be allowed to run PER-dag at once.  
 
#### depends_on_past (bool) 
when set to true, task instances will run squenctially after previous schedule of the task gets succeeded.   

#### dag (DAG)
a reference to the dag to which task is attached (if any).

#### priority_task (int)
priority weight of a task against other tasks. This allows the executor to trigger higher priority tasks before others.

#### pool (str) 
a slot pool in which a task should run. Slot pools are a way to limit cincurrency for certain tasks.

 
