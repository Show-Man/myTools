# -*- coding:utf-8 -*-
from dateutil.relativedelta import relativedelta
import os
import datetime as dt
import requests
import pyminizip
import zlib
import configparser

# DEBUG：来月と過程する
#now         = dt.datetime.now() + relativedelta(months=1)
#last_month  = (now - relativedelta(months=1)).strftime('%m')

now           = dt.datetime.now()
last_month    = (now - relativedelta(months=1)).strftime('%m')
year        = now.strftime('%Y')
month       = now.strftime('%m')
day         = now.strftime('%d')

config = configparser.ConfigParser()
config.read('./config.ini', 'UTF-8')

base_path       = config.get('base', 'path')
base_dir_name   = config.get('base', 'dirname').replace('yyyy', year).replace('MM', last_month).replace('YMD', '{0:%Y%m%d}'.format(now))
base_file_name  = config.get('base', 'filename').replace('yyyy', year).replace('MM', last_month)

# /yyyyMM 直下にディレクトリを生成する
target_dir = os.path.join(base_path, year + last_month, base_dir_name)
if not os.path.exists(target_dir):
    os.system('mkdir ' + target_dir)

# '草案' ファイルの中の日付（%yyyy%, %m%, %MM%, %dd）を適切な日時に置き換え
draft_with_path = os.path.join(base_path, year + last_month, '草案')
with open(draft_with_path + '.txt', encoding='utf-8') as file:
    contents = file.read()
contents = contents.replace('%yyyy%', year)
contents = contents.replace('%m%', last_month)
contents = contents.replace('%MM%', month)
contents = contents.replace('%dd%', day)

with open(draft_with_path + '.txt', mode='w', encoding='utf-8') as file:
    file.write(contents)

# /yyyyMM 直下にある '草案.txt' を、/yyyyMM 直下に生成したディレクトリ配下にコピーする
copy_from   = draft_with_path + '.txt'
copy_to     = os.path.join(target_dir, base_file_name + '.txt')
if not os.path.exists(copy_to):
    os.system('cp ' + copy_from + ' ' + copy_to)

# パスワード付き zip ファイルを生成
zip_pass = config.get('zip', 'pass')
created_text_with_path = os.path.join(target_dir + '/' + base_file_name)
pyminizip.compress(created_text_with_path + '.txt', '',
                   created_text_with_path + '.zip', zip_pass, 5)

# zip ファイル付きのチケットを生成・送付
fresh_mail      = config.get('freshdesk', 'email')
fresh_subject   = config.get('freshdesk', 'subject')
fresh_source    = config.get('freshdesk', 'source')
fresh_status    = config.get('freshdesk', 'status')
fresh_priority  = config.get('freshdesk', 'priority')
fresh_message   = config.get('freshdesk', 'message')
fresh_domain    = config.get('freshdesk', 'domain')
fresh_api       = config.get('freshdesk', 'apikey')
fresh_pass      = config.get('freshdesk', 'pass')

multipart_data = {
    'email'         : (None, fresh_mail),
    'subject'       : (None, fresh_subject),
    'source'        : (None, fresh_source),
    'status'        : (None, fresh_status),
    'priority'      : (None, fresh_priority),
    'attachments[]' : (base_file_name + '.zip', open(created_text_with_path + '.zip', 'rb'), 'application/zip'),
    'description'   : (None, fresh_message)
}

requests.post(fresh_domain,
              auth = (fresh_api, fresh_pass),
              files = multipart_data)