# keep import to ensure the dag processor parses the file
from airflow.sdk import dag
from dagfactory import load_yaml_dags

load_yaml_dags(globals_dict=globals())
