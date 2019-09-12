# 2進数、8進数、16進数 → 10進数に変換するスクリプト

import sys

args = sys.argv

pattern = int(args[2])  # 2進数=2, 8進数=8, 16進数=16

if len(args) == 3 and (pattern == 2 or pattern == 8 or pattern == 16):
    print(int(args[1], pattern))
else:
    # エラー
    print(" 2進数の場合: python3 to_decimal.py { 2進数の値} 2")
    print(" 8進数の場合: python3 to_decimal.py { 8進数の値} 8")
    print("16進数の場合: python3 to_decimal.py {16進数の値} 16")