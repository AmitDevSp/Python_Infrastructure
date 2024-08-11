import windows_tools.updates as windows_updtes
import windows_tools.installed_software as installed_software
import windows_tools.antivirus as antivirus
import windows_tools.logical_disks as logical_disks
import windows_tools.file_utils as file_utils

updtes = windows_updtes.get_windows_updates()
disks = logical_disks.get_logical_disks()
print(updtes)
print(disks)


