Web VPython 3.2
group1 = group()
import random
box(size = vec(10,15,10),pos = vec(0,0,0),color = color.red,group=group1)
box(size = vec(10,5,5),pos = vec(0,-5,7.5),color = color.red,group=group1)
cylinder(size = vec(10,15,10),pos = vec(-5,6,0),color = color.red,group=group1)
cylinder(size = vec(0.5,5,5),pos = vec(5,1.5,2.5),color = color.yellow)
cylinder(size = vec(0.5,5,5),pos = vec(5.75,1.5,2.5),color = color.yellow)
cylinder(size = vec(0.4,4.5,4.5),pos = vec(5.5,1.5,2.5),color = color.yellow)
cylinder(size = vec(5.5,0.6,0.6),pos = vec(5.5,1.5,4.5),color = color.yellow,axis = vec(0,.5,0))
sphere(pos = vec(5.5,7,4.5),radius = 0.75,color = color.red)
box(size = vec(5,2,2.25),pos = vec(0,-3,8),color = color.blue)
box(size = vec(5.5,1,2.5),pos = vec(0,-2.75,8),color = color.black)
box(size = vec(11,2,17),pos = vec(0,-7,2),color = color.black)
box(size = vec(30,1,30),pos = vec(0,-7,5),texture = textures.wood)
a = box(size = vec(2.25,2.25,2.25),pos = vec(0,3,4),texture = 'https://st.depositphotos.com/1006187/4695/i/450/depositphotos_46951539-stock-photo-number-from-gold.jpg')
b = box(size = vec(2.25,2.25,2.25),pos = vec(3,3,4),texture = 'https://st.depositphotos.com/1006187/4695/i/450/depositphotos_46951539-stock-photo-number-from-gold.jpg')
c = box(size = vec(2.25,2.25,2.25),pos = vec(-3,3,4),texture = 'https://st.depositphotos.com/1006187/4695/i/450/depositphotos_46951539-stock-photo-number-from-gold.jpg')


t = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLGoVu6ZhlYOXpiOESjoBD4F1noL4xHNvHIg&s", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQRlgl0jjLFDtlbRGNL6kXGXCgdzQoLITeww&s", 'https://st.depositphotos.com/1006187/4695/i/450/depositphotos_46951539-stock-photo-number-from-gold.jpg', "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDKcc9d7c-u_qrTYlYXH4iL6a-jTPmLDGIfg&s"]
i = 0
while True :
    rate(100)
    k = keysdown()
    if ' ' in k :   
        a.texture = t[i % 4]
        b.texture = random.choice(t)
        c.texture = random.choice(t)
        i = i + 1
