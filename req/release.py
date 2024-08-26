from managers.azure_manager import release_client, delete
from azure.devops.v7_0.release.release_client import ReleaseClient 
from azure.devops.v7_0.release.models import ReleaseStartMetadata
import config


project_name = 'Project'
TFS_organization_url = config.TFS_organization_url


def get_release(release_id):
    return ReleaseClient.get_release(self=release_client(), project=project_name, release_id=release_id)


def create_release(definition_id):
    release_start_metadata = ReleaseStartMetadata(
        definition_id=definition_id,
        description='New release description',
        artifacts=[],
        is_draft=False,
        reason='manual'

    )

    return ReleaseClient.create_release(self=release_client(), project=project_name, release_start_metadata=release_start_metadata)


def get_all_releases():
    # Azure DevOps REST API typically limits to 50 items
    releases = ReleaseClient.get_releases(self=release_client(), project=project_name)
    return releases


def get_release_definitions():
    release_definitions = ReleaseClient.get_release_definitions(self=release_client(), project=project_name)
    return release_definitions


def get_deployments(definition_id):
    deployments = ReleaseClient.get_deployments(self=release_client(), project=project_name, definition_id=definition_id)
    return deployments


def get_release_environments(release_id):
    release = ReleaseClient.get_release(self=release_client(), project=project_name, release_id=release_id)
    return release.environments


def get_release_environment(release_id, environment_id):
    release_environment = ReleaseClient.get_release_environment(self=release_client(), project=project_name, release_id=release_id, environment_id=environment_id)
    return release_environment


def get_release_artifacts(release_id):
    release = ReleaseClient.get_release(self=release_client(), project=project_name, release_id=release_id)
    if release and release.artifacts:
        return release.artifacts
    else:
        return None


def get_release_variables(release_id):
    release = ReleaseClient.get_release(self=release_client(), project=project_name, release_id=release_id)
    return release.variables


def get_environment_status(release_id, environment_id):
    release_environment = ReleaseClient.get_release_environment(self=release_client(), project=project_name, release_id=release_id, environment_id=environment_id)
    return release_environment.status


def delete_release_definition(definition_id):
    results = ReleaseClient.delete_release_definition(self=release_client(), project=project_name, definition_id=definition_id)
    return results 


def get_release_definition_history(definition_id):
    release_definition_history = ReleaseClient.get_release_definition_history(self=release_client(), project=project_name, definition_id=definition_id)
    return release_definition_history 


def get_release_definition(definition_id):
    release_definition_history = ReleaseClient.get_release_definition(self=release_client(), project=project_name, definition_id=definition_id)
    return release_definition_history 


def get_logs(release_id):
    logs = ReleaseClient.get_logs(self=release_client(), project=project_name, release_id=release_id)
    return logs 


def get_task_log(release_id, environment_id, release_deploy_phase_id, task_id):
    logs = ReleaseClient.get_task_log(self=release_client(), project=project_name, release_id=release_id, environment_id=environment_id, release_deploy_phase_id=release_deploy_phase_id, task_id=task_id)
    log_data = ''.join([chunk.decode('utf-8') for chunk in logs])
    return log_data

