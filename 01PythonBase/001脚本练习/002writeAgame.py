print('------------------')
temp = input("input a number:请输入一个数字：")
guest = int(temp)
while guest != 8:
    temp = input("input a number:请输入一个数字：")
    guest = int(temp)
    if guest == 8:
        print("You love me?")
    else:
        if guest > 8:
            print("输入的数字太大了")
        else:
            print("输入的数字太小了")
print("再试一次!")

#数据类型不对，报错
# input a number:请输入一个数字：nihao
# Traceback (most recent call last):
#   File "F:/PycharmProjects/learnpyton/【01】Python基础开发（零基础入门学习）/001脚本练习/002writeAgame.py", line 3, in <module>
#     guest = int(temp)
# ValueError: invalid literal for int() with base 10: 'nihao'

