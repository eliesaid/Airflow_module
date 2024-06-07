from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import time


def wait_1_minute():
    time.sleep(60)


with DAG(
    dag_id="concurrent_dag",
    schedule_interval=None,
    start_date=days_ago(0),
    doc_md="""# Documented DAG
This `DAG` is documented and the next line is a quote:

> Airflow is nice

This DAG has been made:

* by DataScientest
* with documentation
* with caution
    """
) as dag:

    task1 = PythonOperator(
        task_id="wait1",
        python_callable=wait_1_minute,
    )

    task2 = PythonOperator(
        task_id="wait2",
        python_callable=wait_1_minute,
    )

    task3 = PythonOperator(
        task_id="wait3",
        python_callable=wait_1_minute,
    )