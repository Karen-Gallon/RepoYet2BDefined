'''画一颗花哨的树'''
import turtle
import random

def trunk_and_branch(length):
    if length > 2:
        if 8 <= length <= 12:
            tim.color(random.choice(palette)) #随机树枝颜色假装花蕾花瓣
            tim.pensize(length / 3) #调细树枝
        elif length < 8:
            tim.color(random.choice(palette))
            tim.pensize(length / 2)
        else:
            tim.color('sienna')
            tim.pensize(length / 10)

        r = 1.5 * random.random()#每loop一次都生成1个新随机数
        d = 1.5 * random.random()
        tim.forward(length)
        tim.right(20*r) #于是每次都有不同的角度
        trunk_and_branch(length-10*d) #随机长度
        tim.left(40*r) 
        trunk_and_branch(length-10*d)
        tim.right(20*r) 
        tim.up()
        tim.backward(length) #回退的时候把笔提起来，不然颜色会冲突
        tim.down()
        

palette = ['misty rose','lavender blush','snow','ghost white','lavender','salmon','pink']#好不容易找到的palette, 使劲用        
tim = turtle.Turtle() #调用turtle模块的Turtle方法，创建1只海龟，起名tim, 下面就可以对它颐指气使了
turtle.screensize(bg='linen')
tim.left(90)
tim.up()
tim.backward(350)
tim.down()
trunk_and_branch(75)

turtle.done()
