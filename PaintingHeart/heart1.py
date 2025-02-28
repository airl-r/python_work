# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# 如果运行代码遇到问题，可加群讨论 - QQ群：155816967
# 如用代码进行二创并发布，请在明显处注明来源：Crossin的编程教室，否则将可能成为我下期视频素材[狗头][冷笑]

# 代码使用到 pygame-zero 框架，看起来与一般代码稍有不同，会有很多未定义的方法和变量，
# 在一些编辑器里会报错，但其实是可以运行的，无需手动增加 import。
# pgzero有两种方式运行（https://pygame-zero.readthedocs.io/zh_CN/latest/ide-mode.html）
# 本代码用的是第二种直接运行的方式（需新版pgzero）。
# 有部分读者反馈此代码在spyder上无法运行，类似情况可以尝试第一种传统方法：
# 把最后的pgzrun.go()去掉，然后直接在命令行该目录下运行： pgzrun sheep.py

import pgzrun
from math import pi, sin, cos
import random

# 粒子类，图像上每一个小点都是一个粒子对象
import pgzero


class Particle():
    def __init__(self, pos, size, f):
        self.pos = pos    # 粒子当前位置（后面会变动）
        self.pos0 = pos   # 粒子的原始位置
        self.size = size  # 粒子大小
        self.f = f        # 粒子的随机位移比例

    def draw(self):
        global L
        # 用矩形绘制粒子
        screen.draw.filled_rect(Rect((L*self.f*self.pos[0] + 400, -L*self.f*self.pos[1] + 300), self.size), 'hot pink')

    def update(self, t):
        # 根据程序运行时间计算一个正弦函数作为位移量
        # 如果要调整爱心跳动的频率、幅度等效果，可修改这里面的数字
        df = 1 + (4 - 3 * self.f) * sin(t * 3) / 12
        self.pos = self.pos0[0] * df, self.pos0[1] * df

tt = [105, 102, 98, 115, 117, 33, 112, 103, 33, 106, 108, 118, 111, 33, 46, 33, 68, 115, 112, 116, 116, 106, 111, 30341, 32535, 31244, 25946, 23461]
no_p = 20000
dt = 2*pi/no_p
particles = []
t = 0
c = 0
# 采用极坐标下的爱心曲线，计算出爱心图案上的基准点，创建粒子对象
# 每个点会有一个延轴向的随机位移，随机采用正态分布
while t < 2*pi:
    c += 1
    sigma = 0.15 if c % 5 else 0.3
    f = 1 - abs(random.gauss(1, sigma) - 1)
    x = 16*sin(t)**3
    y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
    size = (random.uniform(0.5,2.5), random.uniform(0.5,2.5))
    particles.append(Particle((x, y), size, f))
    t += dt

def draw():
    screen.clear()
    # 绘制爱心粒子
    for p in particles:
        p.draw()

    if L == 10:
        # 采用同样原理，绘制外层大爱心，但生成粒子，只是每帧随机绘制
        t = 0
        while t < 2*pi:
            f = random.gauss(1.1, 0.1)
            x = 16*sin(t)**3
            y = 13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t)
            size = (random.uniform(0.5,2.5), random.uniform(0.5,2.5))
            screen.draw.filled_rect(Rect((10*f*x + 400, -10*f*y + 300), size), 'hot pink')
            t += dt * 3
    screen.draw.filled_rect(Rect((-10*11 + 400, 11*20 + 200), (2, 2)), 'hot pink')

TITLE = ''.join([chr(i-1) for i in tt])
status = 0
L = 100
elapsed = 0
def update(dt):
    global elapsed, L, status
    elapsed += dt
    if status == 0:
        # 为了初始的集聚效果，加了一个很大的倍数L，并不断缩小至正常值
        L -= dt * 200
        if L <= 10:
            status = 1
            L = 10
    elif status == 2:
        L += dt * 200
    # 根据时间更新粒子位置
    for p in particles:
        p.update(elapsed)

TITLE = 'heart of ikun - Crossin的编程教室'

pgzrun.go()


