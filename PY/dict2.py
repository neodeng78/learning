"""

字典的常用操作

Neo edit
verson 2.0
"""


def main():
	stu = {'name': 'neo', 'age': 41, 'gender': True,'hobby':'tennis'}
	print(stu)
	print(stu.keys())
	print(stu.values())
	print(stu.items())

	for elem in stu.items():
		print(elem)
		print(elem[0], elem[1])
	if 'age' in stu:
		stu['age'] = 20
	print(stu)
	stu.setdefault('score', 60)
	print(stu)
	stu.setdefault('score', 100)
	print(stu)
	stu['score'] = 100
	print(stu)


if __name__ == '__main__':
	main()
