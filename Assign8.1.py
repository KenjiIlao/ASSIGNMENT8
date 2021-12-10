import random
FirstNumber = random.randint(0,9)
SecondNumber = random.randint(0,9)
ThirdNumber = random.randint(0,9)

while True:
     First = int(input ('Enter the first jackpot number : '))
    
     Second = int(input ('Enter the second jackpot number : '))
     
     Third = int(input ('Enter the third jackpot number : '))

     if First == FirstNumber:
        if Second == SecondNumber:
            if Third == ThirdNumber:
                print ('Winner')
                print (f'The lucky random numbers are {FirstNumber}, {SecondNumber}, {ThirdNumber}.')
                break
            else:
                print ('You Loss')
                print ('Try Again')
                Choose = input('Yes or No:')
                if Choose == "No":
                    print (f'The lucky random numbers are {FirstNumber}, {SecondNumber}, {ThirdNumber}.')
                    break
        else:
            print ('You loss')
            print ('Try Again')
            Choose = input('Yes or No:')
            if Choose == "No":
                print (f'The lucky random numbers are {FirstNumber}, {SecondNumber}, {ThirdNumber}.')
                break
     else:
        print ('You Loss')
        print ('Try Again')
        Choose = input('Yes or No:')
        if Choose == "No":
            print (f'The lucky random numbers are {FirstNumber}, {SecondNumber}, {ThirdNumber}.')
            break