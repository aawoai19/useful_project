# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import win32com.client
import time

new_list = {
    'name':[],
    'id':[],
    'path':[]
}
list = new_list
while True:
    wmi=win32com.client.GetObject('winmgmts:')
    for p in wmi.InstancesOf('win32_process'):
        # print p.Name, p.Properties_('ProcessId'),p.Properties_('ExecutablePath')
        new_list['name'].append(p.Name)
        new_list['id'].append(p.Properties_('ProcessId'))
        new_list['path'].append(p.Properties_('ExecutablePath'))

    for key in range(len(list['name'])):
        if list['name'][key] not in new_list['name']:
            print list['name'][key],'is closed'
            print list['path'][key]
    for key in range(len(new_list['name'])):
        if new_list['name'][key] not in list['name']:
            print new_list['name'][key],'is new open'
            print new_list['path'][key]

    list = new_list
    new_list = {
        'name':[],
        'id':[],
        'path':[]
    }
    time.sleep(1)