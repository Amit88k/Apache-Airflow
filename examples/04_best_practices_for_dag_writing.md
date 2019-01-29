There are always some points which every one should follow for clean code. Some points related to Airflow are

#### 1. Scope
The DAG must appear in globals() scope. Airflow loads dags with global scope only. Consider the following two DAGs. Only dag_1 will be loaded; the other one only appears in a local scope.

##### dag 1
	dag_1 = DAG('this_dag_will_be_discovered')
	
##### dag 2
	def my_function();
		dags_2 = DAG('but_this_dag_will_not')
		
	my_function()
	
Sometimes it can be useful to put a dag in local scope. For example, a common pattern with SubDagOperator define inside a function so that Airflow doesn't try to load it as a standalone DAG.

#### 2. start_date
It is recommended to use constants for start_date parameter, because dynamic ones would act unpredictable based on with your airflow pipleline is evaluated by the scheduler.

link : https://airflow.apache.org/faq.html#what-s-the-deal-with-start-date







