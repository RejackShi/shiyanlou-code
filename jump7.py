#这是什么玩意儿
#今天加一个单词：wrapper(),是修饰器的函数。

for num in range(100):
	num += 1
	if num%10 == 7 or num%7 == 0 or num//10 == 7:
		continue
	print(num)
