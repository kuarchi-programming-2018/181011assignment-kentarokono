# coding: utf-8
'''
演習課題「スライムの合計体重を出力！」
右側のコードエリアにあるプログラムは、出現するスライムの匹数をランダムに生成します。
スライムの体重は、すべて体重100キロです。そして、
「体重100キロのスライムがXX匹あらわれた」と表示します。

そこで、スライムの合計体重を計算して、「スライムの合計体重はYYキロです」と表示してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

 期待する出力値
体重100キロのスライムがXX匹あらわれた
スライムの合計体重はYYキロです
'''
import random
number = random.randint(1, 10)  # 匹数 1 ～ 10
print("体重100キロのスライムが" + str(number) + "匹あらわれた")
# 合計体重 = 匹数 x 100

解答
# coding: utf-8
import random
slime_weight=100 #スライムの体重
slime_num=random.randint(1,10) #スライムの数
total=slime_weight*slime_num
print("体重100キロのスライムが" + str(slime_num) + "匹あらわれた")
print("スライムの合計体重は"+str(total)+"キロです")