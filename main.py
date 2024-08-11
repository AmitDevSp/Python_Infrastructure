from managers import azure_manager, vSphere_manager, windows_manager
from utility import azure_utility, vSphere_utility, files_utility
from req import pipeline, release, tests, work_item, tests

pbi_id = 321321
azure_release_id = 123123

release_ids = [azure_release_id]
azure_utility.deep_clear_pbi_relations(pbi_id)