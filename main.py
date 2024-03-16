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
                "type": "SUB_WORKFLOW",
                "taskReferenceName": "MaSubWorkflow_Test_F12KK8",
            },
            {
                "subWorkflowParam": {
                    "name": "MaSubWorkflow_Test",
                    "version": "1",
                },
                "type": "SUB_WORKFLOW",
                "taskReferenceName": "MaSubWorkflow_Test_F12KK9",
            },
        ],
        "dynamicTasksInput": {
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
