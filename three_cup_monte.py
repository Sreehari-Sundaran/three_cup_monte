from random import shuffle
def shuffle_list(mylist): #function for shuffling the cups
    shuffle(mylist)
    return mylist
mylist=['','0','']
shuffle_list(mylist)


def player_guess(): #function for getting number from player
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number 0,1 and 2')
    return int(guess)


def check_guess(mylist,guess): #validation of the input and shuffled
    if mylist[guess] == 'O':
        print('Correct Guess!')
    else:
          print('Wrong! Better luck next time')
print(mylist)


#inital list
mylist=['','0','']

#shuffle list
mixedup_list=shuffle_list(mylist)

#user guess
guess=player_guess()

#check guess
check_guess(mixedup_list,guess)