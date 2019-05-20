# -*- coding: utf-8 -*-

from jira import JIRA
from manipule_json import get_fields_values

jira = JIRA(server='url-jira', basic_auth=('user.jira', 'password'))

def cerate_dic_fields(webhook_json):
    summary, description, priority, fields_value = get_fields_values(webhook_json)

    dic_field = {
        'project': {'key': 'ISSUE'},
        'summary': summary,
        'description': description,
        'issuetype': {'id': 'id'},
        'customfield_25253': 'name1-customfield',              
        'customfield_25254': 'name2-customfield',             
        'customfield_25348': 'name3-customfield',         
        'customfield_25252': 'name4-customfield'               
    }

    return dic_field

def create_new_issue(dic_field):
    return jira.create_issue(dic_field, prefetch = True)

def coment_issue():
    jira.add_comment('ISSUE-999', 'Hello World!')
