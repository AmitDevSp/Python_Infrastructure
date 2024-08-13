from managers.azure_manager import build_client
from azure.devops.v7_0.build.build_client import BuildClient
import config


project_name = 'Project'
TFS_organization_url = config.TFS_organization_url


def get_build(build_id):
    build = BuildClient.get_build(self=build_client(), project=project_name, build_id=build_id)
    return build


def get_builds():
    build = BuildClient.get_builds(self=build_client(), project=project_name)
    return build

def get_changes_between_builds(from_build, to_build):
    changes = BuildClient.get_changes_between_builds(self=build_client(), project=project_name, from_build_id=from_build, to_build_id=to_build)
    return changes


def get_latest_build(definition_id):
    latest_build = BuildClient.get_latest_build(self=build_client(), project=project_name, definition=definition_id)
    return latest_build


def add_build_tag(build_id, tag):
    build_tag = BuildClient.add_build_tag(self=build_client(), project=project_name, build_id=build_id, tag=tag)
    return build_tag


def get_build_timeline(build_id):
    build_timeline = BuildClient.get_build_timeline(self=build_client(), project=project_name, build_id=build_id)
    return build_timeline


def get_build_logs(build_id):
    build_timeline = BuildClient.get_build_logs(self=build_client(), project=project_name, build_id=build_id)
    return build_timeline


def get_build_log_lines(build_id, log_id):
    build_timeline = BuildClient.get_build_log_lines(self=build_client(), project=project_name, build_id=build_id, log_id=log_id, end_line=20)
    return build_timeline


def get_artifacts(build_id):
    build_timeline = BuildClient.get_artifacts(self=build_client(), project=project_name, build_id=build_id)
    return build_timeline



