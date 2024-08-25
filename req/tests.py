from managers.azure_manager import test_client
from azure.devops.v7_0.test.test_client import TestClient
from datetime import datetime, timedelta,timezone
import config
import json


project_name = 'Project'
TFS_organization_url = config.TFS_organization_url


def get_release_tests_results(release_id, environment_id):
    run_id = get_test_run_id(release_id, environment_id)
    test_results = get_test_results(run_id=run_id)
    return test_results


def get_test_run_id(release_id, environment_id):
    now = datetime.now(timezone.utc)
    minDate = now - timedelta(days=6)

    query = {
        "project": project_name,
        "min_last_updated_date": minDate,
        "max_last_updated_date": now,
        "release_ids": [release_id],
        "release_env_ids": [environment_id]
    }  
    test_runs = TestClient.query_test_runs(self=test_client(), **query)
    return test_runs[0].id


def get_test_results(run_id):
    results = TestClient.get_test_results(self=test_client(), project=project_name, run_id=run_id)
    return results


def get_test_result_attachments(run_id, test_case_result_id):
    attachments = TestClient.get_test_result_attachments(self=test_client(), project=project_name,run_id=run_id,test_case_result_id=test_case_result_id)
    return attachments


def get_test_cases_from_suite(plan_id, suite_id):
    test_suite_entries = TestClient.get_test_cases(self=test_client(), project=project_name, plan_id=plan_id, suite_id=suite_id)
    return test_suite_entries


def add_test_cases_to_suite(plan_id, suite_id, test_case_ids):
    test_suite_entries = TestClient.add_test_cases_to_suite(self=test_client(), project=project_name, plan_id=plan_id, suite_id=suite_id, test_case_ids=test_case_ids)
    return test_suite_entries


