# 10進数 → 2進数、8進数、16進数に変換するスクリプト

import sys

args = sys.argv

# 引数が 2 つ以上あるとアウト
if len(args) == 2:
    num = int(args[1])
    print(' 2進数: ' + bin(num))     # 2進数
    print(' 8進数: ' + oct(num))     # 8進数
    print('16進数: ' + hex(num))     # 16進数
else:
    print("引数は必ず 1 つですよ〜！")
    sys.exit()