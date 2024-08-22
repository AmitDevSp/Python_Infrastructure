from pyVmomi import vim
import time


def print_all_vms_in_inventory(connection):
    try:
        content = connection.RetrieveContent()
        
        container_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.VirtualMachine],
            True
        )

        for vm in container_view.view:
            print(vm.name)
    except Exception as e:
        print(f"Error listing virtual machines: {e}")


def find_folder_recursively(folder, target_folder_name):
    if folder.name == target_folder_name:
        return folder

    for child in folder.childEntity:
        if isinstance(child, vim.Folder):
            result = find_folder_recursively(child, target_folder_name)
            if result:
                return result

    return None


def wait_for_task(task, actionName='job', hideResult=False):
    while task.info.state in [vim.TaskInfo.State.running, vim.TaskInfo.State.queued]:
        time.sleep(2)
    
    if task.info.state == vim.TaskInfo.State.success:
        if task.info.result is not None and not hideResult:
            out = '%s completed successfully, result: %s' % (actionName, task.info.result)
            print(out)
        else:
            out = '%s completed successfully.' % actionName
            print(out)
    else:
        out = '%s did not complete successfully: %s' % (actionName, task.info.error)
        raise task.info.error
        print(out) 
    return task.info.result