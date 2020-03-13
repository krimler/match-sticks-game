####################################
#!/opt/anaconda3/bin/python
####################################
# Match Sticks Game!
# There are 21 match stiks.
# User can pick up matchistics at max 4. Miminum one should be picked.
# Computer also does the same.
# Whoever is forced to pick up last matchstick, is loser.
#
####################################
import numpy as np
####################################
computer_always_win = True
####################################
def choice(val, prob, others):
    other_prob = prob/len(others)
    other_probs = [other_prob] * len(others)
    z = np.random.choice(others, 1, other_probs)
    z = z[0]
    pop = [val, z]
    other_prob = 1.0 - prob
    weights = [prob, other_prob]
    k = 1
    ans = np.random.choice(pop, k, weights)
    ans = ans[0]
    return ans
####################################
def draw(n):
    assert(n > 0)
    print("we got " + str(n) + " matchsticks!")
    i = n
    while(i > 0):
        if (i< 5):
            for j in range(i):
                print('!', end ="")
            break
        i -= 5
        print('[!!!!!] ', end ="")
    print("")    
####################################
def greet_loser(loser, winner):
    print("You lose " + loser + " !")
    print("Bye Bye Loser baby!")
    print("Congrats " + winner +  ' ! XOXO :->')
####################################
def gen_range(n):
    assert(n > 0)
    r = []
    if n >= 4 :
        r = list(range(1, 5))
    else:
        r = list(range(1, n+1))
    print(r)
    return r
####################################
def play():
    global computer_always_win
    n = 21
    name = input("Please enter your name :")
    while(n > 0):
        draw(n)
        print("")
        if n == 1:
            g = input("Please pick up 1 match stick to be loser : ")
        elif n < 4:
            g = input("Please pick up any match stick from 1 to " + str(n) + " : ")
        else:
            g = input("Please pick up any match stick from 1 to 4 : ") 
        try:
            g = int(g)
        except:
            print("I did not understand!")
            continue
        if not(g > 0 and g < 5 and g <=n):
            print("DUMB!!!!! Please pick up any match stick from 1 to 4 : ")
            continue
        n -= g
        if (n <= 0):
            greet_loser(name, 'computer')
            break
        k = (5 - g)
        if not computer_always_win:
            k = choice(k, 0.999, gen_range(n))
        n -= k
        print("OK! Computer picks up " + str(k))
        if (n <= 0):
            greet_loser('computer', name)
            break
####################################            
play()  
####################################      
