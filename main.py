Web VPython 3.2
group1 = group()
import random
box(size = vec(10,15,10),pos = vec(0,0,0),color = color.red,group=group1)
box(size = vec(10,5,5),pos = vec(0,-5,7.5),color = color.red,group=group1)
cylinder(size = vec(10,15,10),pos = vec(-5,7,0),color = color.red,group=group1)
cylinder(size = vec(0.5,5,5),pos = vec(5,1.5,2.5),color = color.yellow)
cylinder(size = vec(0.5,5,5),pos = vec(5.75,1.5,2.5),color = color.yellow)
cylinder(size = vec(0.4,4.5,4.5),pos = vec(5.5,1.5,2.5),color = color.yellow)
stick = cylinder(size = vec(5.5,0.6,0.6),pos = vec(5.5,1.5,4.5),color = color.yellow,axis = vec(0,.5,0))
ball = sphere(pos = vec(5.5,7,4.5),radius = 0.75,color = color.red)
coolstick = compound( [stick, ball] )
coolstick.pos = vec(5.5,5,4)
coolstick.axis = vec(0,0,-180)
#compound
box(size = vec(5,2,2.25),pos = vec(0,-3,8),color = color.blue)
box(size = vec(5.5,1,2.5),pos = vec(0,-2.75,8),color = color.black)
#box(size = vec(.5,.5,16),pos = vec(5,-2.5,2.5),color = vector(255,140,0))
#box(size = vec(.5,.5,16),pos = vec(-5,-2.5,2.5),color = vector(255,140,0))
#box(size = vec(10,0.5,0.5),pos = vec(0,-2.5,-5.25),color = vector(255,140,0))
#box(size = vec(10,0.5,0.5),pos = vec(0,-2.5,10.25),color = vector(255,140,0))
#box(size = vec(0.5,4,0.5),pos = vec(-5,-4.25,10.25),color = vector(255,140,0))
#box(size = vec(0.5,4,0.5),pos = vec(5,-4.25,10.25),color = vector(255,140,0))
#box(size = vec(0.5,4,0.5),pos = vec(-5,-4.25,-5.25),color = vector(255,140,0))
#box(size = vec(0.5,4,0.5),pos = vec(5,-4.25,-5.25),color = vector(255,140,0))
#yellowthings
box(size = vec(12,2,17),pos = vec(0,-7,2.5),color = color.black)
box(size = vec(35,0.25,35),pos = vec(0,-7,5),texture = textures.wood)
#model
tx = text(text='press spacebar = roll', align='center', color=color.green, pos = vec(0,16,0))
#text
a = box(size = vec(2.25,2.25,2.25),pos = vec(0,3,4.25),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz5VpOnq0QV42xLKefxzIvXA8G7P3QDwP5lw&s')
b = box(size = vec(2.25,2.25,2.25),pos = vec(3,3,4.25),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz5VpOnq0QV42xLKefxzIvXA8G7P3QDwP5lw&s')
c = box(size = vec(2.25,2.25,2.25),pos = vec(-3,3,4.25),texture = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz5VpOnq0QV42xLKefxzIvXA8G7P3QDwP5lw&s')
box(size = vec(2.5,2.5,2.25),pos = vec(0,3,4),color = color.black)
box(size = vec(2.5,2.5,2.25),pos = vec(3,3,4),color = color.black)
box(size = vec(2.5,2.5,2.25),pos = vec(-3,3,4),color = color.black)
#slot
i = 0

t = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLGoVu6ZhlYOXpiOESjoBD4F1noL4xHNvHIg&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQRlgl0jjLFDtlbRGNL6kXGXCgdzQoLITeww&s", 'https://st.depositphotos.com/1006187/4695/i/450/depositphotos_46951539-stock-photo-number-from-gold.jpg', "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDKcc9d7c-u_qrTYlYXH4iL6a-jTPmLDGIfg&s"]
#t = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUWln-ngj5DvcIOzSe3QmWC3RI7xM7JbUXNA&s","data:image/png;base64,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"]
while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        coolstick.axis = vec(-1,4,0)
        coolstick.pos = vec(6,2,6)
        a.texture = t[i % 4]
        b.texture = random.choice(t)
        c.texture = random.choice(t)
        i = i + 1 
#roulette
