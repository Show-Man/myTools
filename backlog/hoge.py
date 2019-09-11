import datetime as dt
import configparser
import requests

now     = dt.datetime.now()
year    = now.strftime('%Y')
month   = now.strftime('%m')

config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

base_url    = config.get('backlog', 'host')
api_key     = config.get('backlog', 'api')

payload = {
    'projectId'     : config.get('backlog', 'projectId'),
    'issueTypeId'   : config.get('backlog', 'issueTypeId'),
    'priorityId'    : config.get('backlog', 'priorityId'),
    'categoryId[]'  : [ config.get('backlog', 'categoryId_01') ],
    'assigneeId'    : config.get('backlog', 'assigneeId'),
    'summary'       : config.get('backlog', 'summary').replace('yyyy', year).replace('MM', month),
}

requests.post('https://' + base_url + '/api/v2/issues', params = { 'apiKey': api_key }, data = payload)