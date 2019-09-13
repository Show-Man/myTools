# ASCII  → 文字に変換するスクリプト

import sys

args = sys.argv

msg = 'ASCII: ' + str(args[1]) + ' → char: ' + str(chr(int(args[1])))
print(msg)