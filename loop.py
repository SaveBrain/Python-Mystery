# now we learn about loop 
'''for i in range (10):
    print('I want to be a great programmer')'''


# akhane i variable ti bebohar korar karon hocche, i er man 0 theke shuru kore ak ak kore barbe abong shorboccho man hobe n-1
'''for i in range (5):
    print(i)'''
    

# amra akhon akta choto program korbo jar kaj hocche 50 ti 1 jog kora. jogfol rakhar jonno result name a akti variable bebohar korbo r loop er jonno i.
'''result = 0 

for i in range (50):
    result = result +1
print(result)'''



# uporer program a kintu amra i variable ti bebohar korchi nah. shekhetre i er bodole underscore symbol bebohar kore program ti korte pari 
#By using _ instead of i, it makes it clear to other programmers reading the code that the loop variable is not being used inside the loop.
'''result = 0
for _ in range (50):
    result = result + 1 
print(result)'''


# akhon 1+2+3+......+50 er jogfol ber korbo. orthat 1 theke 50 porjonto protiti purno shongkha jog kore jogfol dekhate hobe. akhane aktu betikrom royeche 
# ager bar jemon proti bar 1 jog korechilam, abare prothome 1 tarpor 2 tarpor 3 avabe 50 porjonto shongkha gulo jog korte hobe
# ajonno amra   result = result + 1 na likhe, likhbo result = result + num, r ai num er man prothome hobe 1 tarpor 2 avabe protibar 1 barbe 
'''result = 0
num = 1
for _ in range (50):
    result = result + num
    num = num + 1
print(result)'''


# ammra code ti ka aro aktu modify kore likhte pari 
'''result = 0
for num in range(51):
    result = result + num
print(result)'''

# range ( start, n ) . aikhane i er man start theke shuru kore 1 kore barbe abong n-1 a giye shesh hobe 
# amra result = result + num ke onnvabeo likhte pari . like, result += num 
'''result = 0 
for num in range(1,51):
    result += num
print(result)'''



# amra jodi chai je for loop er moddhe 1 kore na bere 5 kore barbe shetawo possible 
'''for i in range(1,20,5,):
    print(i)'''


# loop bebohar kore akti list er shobcheye boro shonkha ber korbo 
'''numbers = [6,1,3,0,9,3,2,5]
max_n = numbers[0]
for n in numbers:
    if n > max_n:
        max_n = n 
        
max_n'''


# akhon amra dekhbo 1 theke 100 porjonto jeshob shongkha 5 dara nishsheshe bivajjo ( orthat 5 dara vag korle vagshesh hoy 0 ) 
'''result = 0
for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num
print('sum is : ', result)'''


# program ti amra aro easy kore korte pari
'''result = 0 
for num in range(5, 101, 5):
    print(num)
    result += num
print('Sum is : ', result)'''



n = 11

for i in range(1,n):
    print(i)