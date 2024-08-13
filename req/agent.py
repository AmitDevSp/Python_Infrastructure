from os import name
from managers.azure_manager import task_agent_client
from azure.devops.v7_0.task_agent.task_agent_client import TaskAgentClient
from azure.devops.v7_0.task_agent.models import TaskAgent

import config


project_name = 'Project'
TFS_organization_url = config.TFS_organization_url


def get_agent(pool_id, agent_id):
    build = TaskAgentClient.get_agent(self=task_agent_client(), pool_id=pool_id, agent_id=agent_id)
    return build


def get_agents(pool_id):
    build = TaskAgentClient.get_agents(self=task_agent_client(), pool_id=pool_id)
    return build


def get_agent_pools():
    pools = TaskAgentClient.get_agent_pools(self=task_agent_client())
    return pools


def get_agent_pool(pool_id):
    pools = TaskAgentClient.get_agent_pool(self=task_agent_client(), pool_id=pool_id)
    return pools


def enable_agent(pool_id, agent_id):
    agent = TaskAgent(
        id=agent_id,
        enabled=True
    )
    pools = TaskAgentClient.update_agent(self=task_agent_client(), pool_id=pool_id, agent_id=agent_id, agent=agent)
    return pools


def disable_agent(pool_id, agent_id):
    agent = TaskAgent(
        id=agent_id,
        enabled=False,
    )
    pools = TaskAgentClient.update_agent(self=task_agent_client(), pool_id=pool_id,agent_id=agent_id, agent=agent)
    return pools
