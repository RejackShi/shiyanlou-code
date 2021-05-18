#用来打印1-100的不含7和7的倍数

for num in range(100):
	num += 1
	if num%10 == 7 or num%7 == 0 or num//10 == 7:
		continue
	print(num)
