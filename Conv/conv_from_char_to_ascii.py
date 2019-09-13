# 文字 → ASCII、に変換するスクリプト

import sys

args = sys.argv

ascii = ''
for char in args[1]:
    ascii += str(ord(char)) + ' '

msg = 'char: ' + str(args[1]) + ' → ASCII: ' + ascii
print(msg)