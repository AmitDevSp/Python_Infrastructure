from pyVim import connect
from pyVmomi import vim
import xml.etree.ElementTree as ET
import ssl
import config


vCenter_Cred = config.vCenter_Cred
ssl_context = ssl._create_unverified_context()


def read_credentials_from_xml(vCenter_Cred=vCenter_Cred):
    try:
        tree = ET.parse(vCenter_Cred)
        root = tree.getroot()
        
        vcenter_host_element = root.find("./vcenter/host")
        vcenter_username_element = root.find("./vcenter/username")
        vcenter_password_element = root.find("./vcenter/password")

        if vcenter_host_element is not None:
            vcenter_host = vcenter_host_element.text
        else:
            raise ValueError("vCenter Host not found in XML.")

        if vcenter_username_element is not None:
            vcenter_username = vcenter_username_element.text
        else:
            raise ValueError("vCenter Username not found in XML.")

        if vcenter_password_element is not None:
            vcenter_password = vcenter_password_element.text
        else:
            raise ValueError("vCenter Password not found in XML.")

        return vcenter_host, vcenter_username, vcenter_password
    
    except Exception as ex:
        print(f"Failed to read credentials from xml. exception: {ex}")
        return ''
    
    
def connect_to_vcenter(host, username, password):

    try:
        connection = connect.SmartConnect(
            host=host,
            user=username,
            pwd=password,
            sslContext=ssl_context
        )

        print("Connected to vCenter successfully.")
        return connection
    except vim.fault.InvalidLogin as e:
        print("Invalid login credentials. Please check your username and password.")
        return None
    except Exception as e:
        print(f"Error connecting to vCenter: {e}")
        return None


def disconnect_from_vcenter(connection):
    try:
        connect.Disconnect(connection)
        print("Disconnected from vCenter.")
    except Exception as e:
        print(f"Error disconnecting from vCenter: {e}")


def establish_vcenter_connection():
    vcenter_host, vcenter_username, vcenter_password = read_credentials_from_xml()
    connection = connect_to_vcenter(vcenter_host, vcenter_username, vcenter_password)
    return connection