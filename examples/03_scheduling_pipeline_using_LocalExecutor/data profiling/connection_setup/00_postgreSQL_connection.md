To test your DB connections via the Ad Hoc Query from the Airflow Web UI, Airflow must be connected to your environment. For this, you would have to establish your own connections via the web UI where you an handle informations like hostname, port, login and passwords. The pipeline code you will author will reference the 'conn_id' of the Connection objects.

### NOTE 
Connections can be created and managed using either the UI or environment variables. I am doing using UI.

### NOTE 
In Local Executor mode, I am using PostgreSQL DB, so I am setting up connection to postgreSQL here. Although there is  a default connection to PostgreSQL provided by Airflow, but it didn't work in my case. Consider yourself lucky if it works for you :). 

### Steps to create connection to PostgreSQL (you can also follow, instructions mentioned in postgreSQL_connection_images by images)
1. From Airflow webserver UI, go to admin > connections > create (as shown in postgreSQL_connection_images/image1 and postgreSQL_connection_images/image2)
2. Fill in the [Conn Id] field with a connection ID e.g. postgres_oltp. It is recommended that you use lower-case characters and separate words with underscores (postgreSQL_connection_images/image3).
3. Choose the connection type with the [Conn Type] field, for postgreSQL select postgres.
4. Fill [Host] field with your database server name or address 
5. Fill [schema] field with your database, you mentioned in /Airflow_HOME/airflow.cfg e.g. airflow.
6. Fill [Password] field with the password. It will be encrypted if airflow[crypto] is installed.
7. Save.
8. Refresh the DAGs. 

### NOTE
9. Sometimes, even after creating a connection with all of the necessary credentials on the Airflow UI the database did not show up under the Data Profiling > Ad hoc Query section or you are unable to do Ad hoc Queries. In such a situation install python-postgres adapter, psycopg2: 
##### pip install psycopg2

10. Restart the Airflow web server and scheduler. 

11. Verify postgres_default correctly configured: From airflow webserver UI, go to Data profiling->Ad Hoc Query. Select postgres_default from drop down and run the following query to verify PostgreSQL is connecting correctly.
##### select * from log;
 
12. Verify airflow.cfg changes reflecting. For this from airflow webserver UI, go to Admin -> Configuration, check that airflow.cfg sql_alchemy_conn, executor, expose_config or any changed configuration is as expected.

13. You are done!