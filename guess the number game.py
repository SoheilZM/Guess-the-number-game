import random
def main():
    b='y'
    while b=='y':
        print ("I have the number now you guess it")
        a=random.randint(1,100)
        c=int(input())
        while c!=a:
            if c<a:
                print ('wrong!try again!the number is more than',c)
            if c>a:
                print ('wrong!try again!the number is less than',c)
            c=int(input())
        if c==a:
            print('great')
            print('do you want to play again? if yes send y and press enter')
            b=input()
    while b!='y':
        print ('do you want to play again? if yes send y and press enter else send n')
        b=int(input())
print('welcome to guess the number game')
print("For starting the game send 1 and then press enter")
d=int(input())
while d!=1:
    print("For starting the game send 1")
    d=int(input())
if d==1:
    main()
