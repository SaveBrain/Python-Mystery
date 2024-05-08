# my frist turtle square program
'''import turtle 

turtle.shape("turtle")

turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

turtle.exitonclick()'''


#turle practice code

'''import turtle

turtle.shape("turtle")
turtle.speed(1)

for i in range(3):
    turtle.forward(60)
    turtle.left(60)
    turtle.left(60)
turtle.exitonclick()'''

# akhon amra notun 2 ta functiuon shikhbo jar name hocche penup() and pendown(). penup() mane ami kolom tule fellam, akhon turtle jai print koruk na keno ta screen a show korbe nah (aita kaj cholbe thikie but penup() korar karone screen a kichu show korbe nah)
# abar pendown() korle screen a karjokom shuru hobe   

'''import turtle

turtle.speed(1)

for i in range (20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
    
turtle.exitonclick()'''


    
# borgo-khetro toiri korbo turtle use kore ( for loop ) er dara
'''import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range (4):
    turtle.forward(100)
    turtle.left(90)
turtle.exitonclick()'''


# akhon amra loop er vitore loop chaliye akti turtle program korbo
# এরপর, for side_length in range(50,100,10): লুপের মাধ্যমে আমরা বর্গের প্রতিটি পাশের দৈর্ঘ্য নির্ধারণ করেছি। range(50,100,10) ব্যবহার করে আমরা বর্গের পাশের দৈর্ঘ্য বাড়ানোর জন্য ব্যবহার করেছি। এটি ৫০ থেকে ১০০ পর্যন্ত ১০ একক বেড়ে যাওয়ার জন্য ব্যবহার হয়েছে
#  এরপরে, for i in range(4): লুপের মাধ্যমে আমরা চারটি বর্গ আকারের প্রতিটি বাহুর দৈর্ঘ্য নির্ধারণ করেছি। এখানে চারটি পাশের জন্য প্রতিটি পাশে বর্গ আকারের প্রতিটি বাহু ড্রো করতে হবে তাই ৪ এর মধ্যে লুপ চালানো হয়েছে।
'''import turtle

turtle.shape("turtle")
turtle.speed(1)

for side_length in range (50,100,10):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


turtle.exitonclick()'''



#
'''import turtle

turtle.color("red")
turtle.speed(5)

counter = 0 
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
    counter += 1
turtle.exitonclick()'''


#
import turtle

height = 5
width = 5 

turtle.shape("turtle")
turtle.speed(2)

turtle.penup()

for y in range(height):
    for x in range(width):
        turtle.dot()
        turtle.forward(20)
    turtle.backward(20*width)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    
turtle.exitonclick()