The sample provides you how a dag file look without making it too complex. 

One thing to note that is this Airflow Python script is really just a configuration file specifying the DAG's structure as code. People 
sometimes think of the DAG definition file as a place where they can do some actual data processing - that is not the case at all! The
script’s purpose is to define a DAG object. It needs to evaluate quickly (seconds, not minutes) since the scheduler will execute it
periodically to reflect the changes if any.
