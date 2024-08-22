from managers.azure_manager import pipelines_client
from azure.devops.v7_0.pipelines.pipelines_client import PipelinesClient 
import config


project_name = 'Project'
TFS_organization_url = config.TFS_organization_url


def get_pipeline(pipeline_id):
    return PipelinesClient.get_pipeline(self=pipelines_client(), project=project_name, pipeline_id=pipeline_id)


def pipelinesClient():
    return PipelinesClient.list_pipelines(self=pipelines_client(), project=project_name)


