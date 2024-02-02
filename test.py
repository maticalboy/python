
# 摄氏温度转华氏温度
# 接收用户输入
# celsius = float(input('输入摄氏温度: '))
# 计算华氏温度
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' %(celsius,fahrenheit))

# 交换变量
# a=input('a=')
# b=input('b=')
# a,b=b,a
# print('a=%s,b=%s'%(a,b))

# 生死小游戏
# 30 个人在一条船上，超载，需要 15 人下船。
# 于是人们排成一队，排队的位置即为他们的编号。
# 报数，从 1 开始，数到 9 的人下船。
# 如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
# def game(peopleNum,saveNum,instruct):
    # 初始化 字典
    # people={}
    # 所有人都在船上
    # for i in range(1,peopleNum+1):
    #     people[i]=1
    # 下船的人数
    # downNum=0
    # 当前报号者的编号
    # currNum=1
    # 当前报的数字
    # currInstruct=1
    # while downNum<peopleNum-saveNum:
        # 当前位置超了 从第一个开始
        # if(currNum>peopleNum):
        #     currNum=1
        # 当前位置没人 下一个
        # if(people[currNum]==0):
        #     currNum+=1
        #     continue
        # 当前位置有人 判断走不走
#         if(currInstruct==instruct):
#             people[currNum]=0
#             print('第%d个人下船'%currNum)
#             currInstruct=1
#             downNum+=1
#             currNum+=1
#         else:
#             currNum+=1
#             currInstruct+=1
#     print('剩下的人编号为{}'.format([i for i in people.keys() if people[i]==1]))
# game(10,1,6)