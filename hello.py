import random

counter = 60  # 赋值整型变量
miles = 1001.3  # 浮点型
name = "John"  # 字符串
d = 4+3j
print(miles ** counter)

print(name, end=" " )
print(type(d))

a = random.random()
print(a)
a = random.uniform(12,20)
print(a)

for x in [1, 2, 3]: print(x, end=" ")
#input("\n\n按下 enter 键后退出。")

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串(




list = [3, 2, 8, 0, 1]
list.sort(key=lambda x: -x)
print (list)  # 降序排序[8, 3, 2, 1, 0]


students = [('john', 'A', 15), ('jane', 'B', 12), ('dave','B', 10)]
print(sorted(students,key=lambda s: s[0])) #按照年龄来排序


list1=[7, -8, 5, 4, 0, -2, -5]
print(sorted(list1,key=lambda x:(x<0,abs(x))))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("透你妈"+basket)
for item in basket:
    print(item)