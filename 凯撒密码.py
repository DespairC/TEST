print('''
======================凯撒加密与解密===========================
===============================================================''')
file_mode = input('''a.txt文件          b.文本
请输入所选模式-->:''')
#模式选择
mode = input('''1.加密             2.解密
请输入所选模式-->：''')
key = input('请输入密位(默认为3)-->：')
etxt = ''

#判断转化
if key == '':    #设置默认为 3
    key = 3
else:
    key = int(key)
if file_mode == 'a':    #模式A  加密或解密txt文件
    trace = input(r'文件地址（?:...\...\..txt）：')
    f = open(trace)
    ftxt = f.read()
elif file_mode == 'b':    #模式B    加密或解密文本
    ftxt = input('请输入加密文本-->:')
else:                     #输错请重新运行
    print('    错误！请再次运行该程序.')
    exit()

#执行加密或解密
for nftxt in ftxt:
    num = ord(nftxt)
#判断模式
    if 97 <= num <= 122:            #判断是否为小写字母
        if mode == '1':
            num = num + key
        elif mode == '2':
            num = num - key                         #其实这里可以全部一起加密位，但或许这样让人看不出来加密密位，挠头。。
        if num < 97:                                  #其实还是很容易看出来，😰😰
            num = num + 26                               #而且这一段有重复，尝试定义一个函数来避免重复，但定义函数后变量又变为不可读。
        elif num > 122:
            num = num - 26
    else:                            #判断是否为其他符号（包括大写字母）
        if mode == '1':
            num = num + key
        elif mode == '2':
            num = num - key
    etxt = etxt + chr(num)

#输出结果
if file_mode == 'a':
    ftxt = open(trace,'w')
    ftxt.write(etxt)
    ftxt.close()
    if mode == '1':
        print('txt文件加密完成')
    elif mode == '2':
        print('txt文件解密完成')
    input()
if file_mode == 'b':
    if mode == '1':
        print('加密文本：%s' %etxt)
    elif mode == '2':
        print('解密文本：%s' %etxt)
    input()
