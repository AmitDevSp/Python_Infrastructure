from managers.azure_manager import core_client
from azure.devops.v7_0.core.core_client import CoreClient 
import config


TFS_organization_url = config.TFS_organization_url


def get_projects():
    return CoreClient.get_projects(self=core_client())


def get_projects_names():
    projects = CoreClient.get_projects(self=core_client())
    names = [proj.name for proj in projects]
    return names