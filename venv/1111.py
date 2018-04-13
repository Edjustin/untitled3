score = (input('请输入一个分数:'))
if score >= 90:
	g = 'A'
elif 60 <= score <= 89:
	g = 'B'
else:
	g = 'C'
print(g)