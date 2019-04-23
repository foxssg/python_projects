#! Python
# A program to simulate coin flips

from numpy import random


##user_number = int(input('How many times do you want to toss a coin?'))
head_count = []
tail_count = []
coin = ['head', 'tail']

##for i in range (0, user_number):
##    a = random.choice(coin)
##    if a == 'head':
##        head_count.append(1)
##    elif a == 'tail':
##        tail_count.append(1)
##
##print('heads = ' + str(sum(head_count)))
##print('tails = ' + str(sum(tail_count)))

flip_coin_tries= []

def flip_coin():
    j = 0
    k = 1
    count = 0
    tries = 0
    while j != k:
        for i in range (0, 4):
            a = random.choice(coin)
            if a == 'head':
                count += 1
            if count == 4:
                j = k
        tries += 1
        #print('heads ' + str(count) + '/4')
        count = 0
        #print('Tries = ' + str(tries))
    percentage = 100 / tries
    #print(percentage)
    flip_coin_tries.append(percentage)


flip_coin_tries= []
for i in range(10000):
    flip_coin()
    
print('% of getting 4/4 flips = ' + str(sum(flip_coin_tries) / 10000))

    

