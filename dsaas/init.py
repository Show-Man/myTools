# -*- coding:utf-8 -*-
import os
import datetime as dt
import configparser

now     = dt.datetime.now()
year    = now.strftime('%Y')
month   = now.strftime('%m')

# 設定ファイルから読み込み
config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

path    = config.get('base', 'path')
fn      = config.get('base', 'filename').replace('yyyy', year).replace('MM', month)

if not os.path.exists(path):
    os.system('mkdir ' + path)

path = os.path.join(path, '{0:%Y%m}'.format(now))
if not os.path.exists(path):
    os.system('mkdir ' + path)

draft_file = os.path.join(path, '草案.txt')
if not os.path.exists(draft_file):
    os.system('cp ./template.txt ' + draft_file)