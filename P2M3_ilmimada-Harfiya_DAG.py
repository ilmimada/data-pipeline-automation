import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'ILMI',
    'start_date': dt.datetime(2024, 1, 8),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=600),
}


with DAG('P2M3_ilmimada_harfiya_etl',
         default_args=default_args,
         schedule_interval='10 9 * * 6',
         catchup=False,
         ) as dag:

    python_extract = BashOperator(
        task_id='python_extract',
        bash_command='sudo -u airflow python /opt/airflow/scripts/extract.py'
    )
    
    ge_validate_clean = BashOperator(
        task_id='ge_validate_clean',
        bash_command='sudo -u airflow python /opt/airflow/scripts/validate_clean.py'
    )

    python_transform = BashOperator(
        task_id='python_transform',
        bash_command='sudo -u airflow python /opt/airflow/scripts/transform.py'
    )

    ge_validate_final = BashOperator(
        task_id='ge_validate_final',
        bash_command='sudo -u airflow python /opt/airflow/scripts/validate_final.py'
    )

    python_load = BashOperator(
        task_id='python_load',
        bash_command='sudo -u airflow python /opt/airflow/scripts/load.py'
    )

python_extract >> ge_validate_clean >> python_transform >> ge_validate_final >> python_load