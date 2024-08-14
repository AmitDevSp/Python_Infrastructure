from azure.devops.connection import Connection, ClientFactoryV7_0
from msrest.authentication import BasicAuthentication
import requests
import config


organization_url = config.TFS_organization_url
personal_access_token = config.TFS_access_token


# ------------------------ #
# use azure-devops package #
# ------------------------ #

try:
    credentials = BasicAuthentication("", personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)
    client_factory = ClientFactoryV7_0(connection)


    def audit_client():
        return client_factory.get_audit_client()


    def accounts_client():
        return client_factory.get_accounts_client()


    def build_client():
        return client_factory.get_build_client()


    def cix_client():
        return client_factory.get_cix_client()


    def client_trace_client():
        return client_factory.get_client_trace_client()


    def contributions_client():
        return client_factory.get_contributions_client()


    def core_client():
        return client_factory.get_core_client()


    def pipelines_client():
        return client_factory.get_pipelines_client()


    def release_client():
        return client_factory.get_release_client()


    def wiki_client():
        return client_factory.get_wiki_client()


    def work_client():
        return client_factory.get_work_client()


    def work_item_tracking_client():
        return client_factory.get_work_item_tracking_client()


    def test_client():
        return client_factory.get_test_client()


    def test_plan_client():
        return client_factory.get_test_plan_client()


    def test_results_client():
        return client_factory.get_test_results_client()
    

    def task_agent_client():
        return client_factory.get_task_agent_client()




except Exception as ex:
    print(f"Failed to connect to Azure DevOps: {ex}")




# ------------------------ #
#      Use REST API        #
# ------------------------ #

def make_request(method, path, verifySSL=False, data=None):
    try:
        response = requests.request(
            method,
            path,
            auth=("", personal_access_token),
            verify=verifySSL,
            json=data,
            headers={'content-type' : 'application/json'}
        )
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def get(path, verifySSL=False):
    return make_request("GET", path, verifySSL)


def post(path, data, verifySSL=False):
    return make_request("POST", path, verifySSL, data)


def put(path, data, verifySSL=False):
    return make_request("PUT", path, verifySSL, data)


def patch(path, data, verifySSL=False):
    return make_request("PATCH", path, verifySSL, data)


def delete(path, verifySSL=False):
    return make_request("DELETE", path, verifySSL)

