#����ʲô�����
#�����һ�����ʣ�wrapper(),���������ĺ�����

for num in range(100):
	num += 1
	if num%10 == 7 or num%7 == 0 or num//10 == 7:
		continue
	print(num)
