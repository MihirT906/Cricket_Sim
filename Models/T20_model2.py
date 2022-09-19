from cgi import test
import numpy as np
import time

def simulate_ball(probs, runs, wickets):
    
    RV = np.random.uniform()*100
    for i in range(1, len(probs)):
        if(RV < probs[i] and RV >= probs[i-1]):
            res = i-1

    if(res == 0):
        result = 'dot'
    elif(res == 1):
        result =  'one'
        runs += 1
    elif(res == 2):
        result =  'two'
        runs += 2
    elif(res == 3):
        result =  'three'
        runs += 3
    elif(res == 4):
        result =  'four'
        runs += 4
    elif(res == 5):
        result =  'five'
        runs += 5
    elif(res == 6):
        result =  'six'
        runs += 6
    elif(res == 7):
        result =  'extra run'
        runs += calculate_extra_runs()
    elif(res == 8):
        result =  'wicket'
        runs += calculate_wicket_runs()
        wickets +=1
    return result, runs, wickets
    
def calculate_extra_runs():
    extra_probs = [84.8034606 ,  6.75192778,  1.20368629,  3.40417529,  3.3101373 ,
        0.        ,  0.52661275]
    for i in range(1, len(extra_probs)):
        extra_probs[i] = extra_probs[i] + extra_probs[i-1]

    extra_probs.insert(0, 0)

    RV = np.random.uniform()*100
    for i in range(1, len(extra_probs)):
        if(RV < extra_probs[i] and RV >= extra_probs[i-1]):
            return i
    return 0

def calculate_wicket_runs():
    wicket_probs = [89.1104006 ,  3.59225127,  0.16926838]
    for i in range(1, len(wicket_probs)):
        wicket_probs[i] = wicket_probs[i] + wicket_probs[i-1]

    wicket_probs.insert(0, 0)

    RV = np.random.uniform()*100
    for i in range(1, len(wicket_probs)):
        if(RV < wicket_probs[i] and RV >= wicket_probs[i-1]):
            return i
    return 0



def simulate_innings(probs):
    wickets = 0
    runs = 0
    for o in range(1,21):
        for b in range(1,7):
            if(wickets==10):
                break
            res,runs, wickets = simulate_ball(probs, runs, wickets)
            #print("" + str(o) + ":" + str(b) + ":" + str(res))
        if(wickets == 10):
            break
        
    return runs, wickets

def test_func(probs):
    arr = [0,0,0,0,0,0,0,0,0]
    for i in range(10000):
        res,runs, wickets = simulate_ball(probs,0,0)
        if(res == "dot"):
            arr[0] += 1
        elif(res == "one"):
            arr[1] += 1
        elif(res == "two"):
            arr[2] += 1
        elif(res == "three"):
            arr[3] += 1
        elif(res == "four"):
            arr[4] += 1
        elif(res == "five"):
            arr[5] += 1
        elif(res == "six"):
            arr[6] += 1
        elif(res == "extra run"):
            arr[7] += 1
        elif(res == "wicket"):
            arr[8] += 1
    #arr = arr/100
    print(arr)



def simulate_game(probs):
    runs1 = 0
    wickets1 = 0
    runs2 = 0
    wickets2 = 0

    runs1, wickets1 = simulate_innings(probs)
    #runs2, wickets2 = simulate_innings(probs)

    #print("----- End of Match -----")
    #print("Team 1 score: " + str(runs1) + "/" + str(wickets1))
    #print("Team 2 score: " + str(runs2) + "/" + str(wickets2))

    if(runs1 > runs2):
        return "Team 1 wins", runs1, wickets1, runs2, wickets2 
    elif(runs1 < runs2):
        return "Team 2 wins", runs1, wickets1, runs2, wickets2 
    else:
        return "Draw", runs1, wickets1, runs2, wickets2 




if __name__ == "__main__":
    probs = [2.98280285e+01, 3.71081235e+01, 6.52753241e+00, 3.19389965e-01,
       1.12894372e+01, 2.79466220e-02, 4.66409159e+00, 5.30686389e+00,
       4.92858640e+00]
    for i in range(1, len(probs)):
        probs[i] = probs[i] + probs[i-1]

    probs.insert(0, 0)
    #test_func(probs)

    runs = []
    wickets = []
    
    for i in range(200000):
        res, runs1, wickets1, runs2, wickets2 = simulate_game(probs)
        runs.append(runs1)
        #runs.append(runs2)
        wickets.append(wickets1)
        #wickets.append(wickets2)
    print("Average runs: " + str(sum(runs)/len(runs)))
    print("Average wickets: " + str(sum(wickets)/len(wickets)))

