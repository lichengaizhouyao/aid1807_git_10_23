# 2048.py项目
matix = [[0 for i in  range(4)]for i in range(4)]
# 用列表推导初始化生成一个4*4的列表,列表元素全为 0
def notzer0(s): #函数的作用:游戏界面上非零的时候才显示,当为0的时候,让其显示为空.
    return s if s!= 0 else '' # 非零的话返回本身,否则返回''


                        
