# Apache-Airflow

Big data pipelines don’t run themselves. Beyond the obvious need to scale pipelines up to large data volumes, theirs is a lot of work that goes into managing dependencies, handling retries, alerting, etc. This need only becomes more pressing as the organization grows and new teams seek to analyze existing data in different ways. As new teams add new pipelines, they generally want to build off the output of existing pipelines and they want to well-defined patterns around retries, alerts, etc so they can focus on the logic of their particular pipeline.  
Workflow management has become such a common need that most companies have multiple ways of creating and scheduling jobs internally. There’s always the good old CRON scheduler to get started. Other simple option is to have scripts call other scripts, and that can work for a short period of time. Eventually simple frameworks emerge to solve problems like storing the status of jobs and dependencies.

# What is Airflow?
1.	An open source WMS to programmatically author, schedule and monitor data pipelines.
2.	Airflow defines tasks and their dependencies as code, executes those tasks on a regular schedule, and distributes task execution across worker processes. 
3.	Airflow offers a rich user experience interface making it easy to visualize pipelines running in production, monitor progress, check the states of currently active and past tasks, shows diagnostic information about task execution, and allows the user to manually manage the execution and state of tasks.
4.	When you have periodical jobs, which most likely involve various data transfer and/or show dependencies on each other, you should consider Airflow.

# Key terms: 
•	Directed Acyclic Graph (DAG):     Airflow uses DAGs to represent workflows. A DAG(as name depicts – a graph without cycle) is a collection of tasks that have directional dependencies. Each node in the graph is a task and edges define dependencies amongst tasks. DAGs describe how to run a workflow.
•	Operators:     While DAGs describe how to run a workflow, Operators determine what actually gets done i.e. trigger a certain action. A DAG is made up of Operators. An operator describes a single task in a workflow. 
So, a DAG is made up of Operators, and together they form a workflow. The DAG defines the sequence and schedule of the operations,  the Operators define discrete tasks that need to take place within this sequence.
•	Tasks: Although the DAG is used to organize tasks and set their execution context, DAGs do not perform any actual computation. Instead, tasks are the element of Airflow that actually “do the work” you want performed. Tasks are generated when instantiating operator objects. The instantiation defines specific values when calling the abstract operator, and the parameterized task becomes a node in a DAG.

# Infrastructure, setup and automation 
3 services are essential for airflow to run as expected:
1.	Airflow Webserver:   A flask server run using gunicorn. Webserver is responsible to serve the UI Dashboard  over http.
2.	Airflow Scheduler: Workflow scheduler is a service that is responsible for the periodic execution of workflows in a reliable and scalable manner. The scheduler is a process that uses DAG definitions in  conjunction with the state of tasks in the metadata database to decide which task need to be executed. The scheduler is generally run as a service.  A daemon built using python-daemon library. Airflow scheduler is more powerful than a cron. 
3.	Airflow Executor: The Executor is a message queuing process that is tightly bound to the scheduler and determines the worker processes that actually execute each scheduled task. There are many types of Executors, each of which uses a specific class of worker processes to execute tasks. For example, the LocalExecutor executes tasks with parallel processes that run on the same machine as the scheduler process. Other Executors, like the CeleryExecutor execute tasks using worker processes that exists on a separate cluster of worker machines. 
4.	Airflow Worker: A wrapper on a celery worker when using Celery Executor. Depending on the size of data and number of tasks that need to be run at a given time, you need to decide on an executor. These are the processes that actually execute the logic of tasks, and are determined by the Executor being used 


# Steps to install Airflow on Linux Machine

# Prerequisites
Python and pip (package manager for python packages) as Airflow is written in Python. If you have not installed already follow the following commands. I am working on python 2.7.5 . Airflow id supported on python 3 as well.
1. sudo yum install python2 (for python 2) or sudo yum install python3 (python 3)
2. Check if installed -> python --version
3. Install pip -> yum install python2-pip or yum install python3-pip
  
# Steps to install Airflow
1. pip install apache-airflow 
	
  # NOTE: GPL dependency
    One of the dependencies of Apache Airflow by default pulls in a GPL library (‘unidecode’). In case this is a concern you can force a non GPL library by issuing export SLUGIFY_USES_TEXT_UNIDECODE=yes and then proceed with the normal installation. Please note that this needs to be specified at every upgrade. Also note that if unidecode is already present on the system the dependency will still be used.

2. export AIRFLOW_GPL_UNIDECODE=yes.
3. export SLUGIFY_USES_TEXT_UNICODE=yes
4. pip install apache-airflow
5. airflow initdb (Initialize Airflow DataBase)
6. Check for UI at: http://host_name:8080

# If some errors related to setuptools, upgrade setuptools first or isntall if not already - pip install --upgrade setuptools and now repeat all the above steps.
