'''画一颗花哨的树'''
import turtle
import random

def trunk_and_branch(length):
    if length > 2:#设定1个停止条件
        #设置画笔颜色、画笔粗细
        if 6 <= length <= 10: #如果树枝短到一定程度了
            tim.pensize(length / 4) #就同时调细笔刷
            tim.color(random.choice(palette)) #同时，把这种树枝当作一种花瓣花蕾，在我指定的花palette里随机选择1个颜色
            
        elif length < 6:
            tim.pensize(length / 4)
            tim.color(random.choice(palette))
            
        else:
            tim.pensize(length / 8)#总体而言，树枝和真实世界一样，越短就越细
            tim.color('saddle brown') #color string大小写、是否空格无所谓，官方已经考虑到这个问题了
            

        r = random.uniform(0, 30)#每loop一次都生成1个新随机浮点数作为新枝旋转角度
        d = random.uniform(0, 15)#新枝减去的长度
        tim.forward(length)
        tim.right(r) 
        trunk_and_branch(length-d) #随机长度
        tim.left(2*r) 
        trunk_and_branch(length-d)
        tim.right(r) 
        tim.up()
        tim.backward(length) #回退的时候把笔提起来，不然颜色会冲突
        tim.down()
        

palette = ['misty rose','lavender blush','snow','ghost white','lavender','salmon','pink']#一共7个颜色可选        
tim = turtle.Turtle() #给我的海龟起个不一样的名字吧
turtle.screensize(bg='linen') #指定画布颜色
tim.left(90)# 头朝上
tim.up()
tim.backward(350) #树根往画布下面放一点
tim.down()
trunk_and_branch(75)

turtle.done()
