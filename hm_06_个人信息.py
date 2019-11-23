# 定义变量保存小明的个人信息
"""
姓名：小明
年龄：18岁
性别：男生
身高：1.75米
体重：75.0公斤
"""

"""
在Python中，定义变量时不需要指定变量的类型
运行时，Python解释器会根据赋值语句等号后侧的数据自动推导出变量中保存数据的准确类型
"""
name = "小明"
age = 18
gender = True
height = 1.75
print(name, age, gender, height)
print(name, name.__class__)
print(age, age.__class__)
print(gender, gender.__class__)
print(height, height.__class__)

print(name, type(name))

xiaoming = {name, age, age, height, gender}
xiao = [name, name, age]
print(xiao, xiao.__class__)
print(xiaoming, xiaoming.__class__)

xiao = 2 ** 1000
print(xiao, xiao.__class__ )
input("输入")








