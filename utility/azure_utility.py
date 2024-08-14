from datetime import datetime
from xmlrpc.client import DateTime
from req import work, release, build, work_item, tests
from utility import files_utility
import re as  regular_expressions


def deep_clear_wi(work_item_id):
    work_item.change_work_item_area(work_item_id, '')
    work_item.change_work_item_iteration(work_item_id, '')
    work_item.remove_target_platform_configuration_from_work_item(work_item_id)
    work_item.change_work_item_state_Removed(work_item_id)
    work_item.change_work_item_description(work_item_id, '')
    work_item.remove_all_work_item_relations(work_item_id)
    print(f"work item {work_item_id} cleared")


def deep_clear_pbi_relations(pbi_id):
    pbi = work_item.get_work_item(pbi_id, work_item.WorkItemExpand.Relations)
    if pbi.relations == None:
        print(f"work item {pbi} has no relations to clear")
        return

    all_pbi_relations_ids = [relation.url[-6:] for relation in pbi.relations]
    for work_item_id in all_pbi_relations_ids:
        wi = work_item.get_work_item(work_item_id)
        if wi.fields['System.State'] == 'Done':
            continue
        deep_clear_wi(work_item_id)
        print(f"work item {work_item_id} cleared")
