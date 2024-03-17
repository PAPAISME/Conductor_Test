from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


@app.get("/api/")
def get_dynamic_fork_parameter():
    return {
        "dynamictasks": [
            {
                "subWorkflowParam": {
                    "name": "MaSubWorkflow_Test",
                    "version": "1",
                },
                "name": "MaSubWorkflow_Test_F12KK7",
                "taskReferenceName": "MaSubWorkflow_Test_F12KK7",
                "type": "SUB_WORKFLOW",
                "inputParameters": {
                    "db_info":{
                        "hostname": "testserver1",
                        "dbname": "F12KK7",
                        "instance": "isttest"
                    }
                },
            },
            {
                "subWorkflowParam": {
                    "name": "MaSubWorkflow_Test",
                    "version": "1",
                },
                "name": "MaSubWorkflow_Test_F12KK8",
                "taskReferenceName": "MaSubWorkflow_Test_F12KK8",
                "type": "SUB_WORKFLOW",
                "inputParameters": {
                    "db_info":{
                        "hostname": "testserver2",
                        "dbname": "F12KK8",
                        "instance": "isttest"
                    }
                },
            },
            {
                "subWorkflowParam": {
                    "name": "MaSubWorkflow_Test",
                    "version": "1",
                },
                "name": "MaSubWorkflow_Test_F12KK9",
                "taskReferenceName": "MaSubWorkflow_Test_F12KK9",
                "type": "SUB_WORKFLOW",
                "inputParameters": {
                    "db_info":{
                        "hostname": "testserver3",
                        "dbname": "F12KK9",
                        "instance": "isttest"
                    }
                },
            },
        ],
        "dynamicTasksInput": {
            "MaSubWorkflow_Test_F12KK7": {
                "dbname": "F12KK7",
            },
            "MaSubWorkflow_Test_F12KK8": {
                "dbname": "F12KK8",
            },
            "MaSubWorkflow_Test_F12KK9": {
                "dbname": "F12KK9",
            },
        },
    }


@app.get("/api/{dbname}")
def get_dbname(dbname: str):
    return {"dbname": dbname}

@app.get("/api/{dbname}/{hostname}/{instance}")
def get_all_info(dbname: str, hostname: str, instance: str):
    return {"hostname": hostname,
            "dbname": dbname,
            "instance": instance
           }
