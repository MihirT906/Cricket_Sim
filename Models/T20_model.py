import numpy as np
import time

def simulate_ball(probs):
    RV = np.random.uniform()*100
    for i in range(1, len(probs)):
        if(RV < probs[i] and RV >= probs[i-1]):
            res = i-1

    if(res == 0):
        return 'dot'
    elif(res == 1):
        return 'one'
    elif(res == 2):
        return 'two'
    elif(res == 3):
        return 'three'
    elif(res == 4):
        return 'four'
    elif(res == 5):
        return 'five'
    elif(res == 6):
        return 'six'
    elif(res == 7):
        return 'extra run'
    elif(res == 8):
        return 'wicket'


def update_score(result, runs, wickets):
    allout = False
    extra = False
    if(result == 'dot'):
        pass
    elif(result == 'one'):
        runs += 1
    elif(result == 'two'):
        runs += 2
    elif(result == 'three'):
        runs += 3
    elif(result == 'four'):
        runs += 4
    elif(result == 'five'):
        runs += 5
    elif(result == 'six'):
        runs += 6
    elif(result == 'extra run'):
        runs += 1
        extra = True
        # Next ball feature
    elif(result == 'wicket'):
        wickets += 1
    if(wickets == 10):
        allout=True
    return runs, wickets, allout,extra


def simulate_game(probs):
    runs1 = 0
    wickets1 = 0
    runs2 = 0
    wickets2 = 0

    for innings in range(2):
        for i in range(20):
            j = 1
            while(j<7):
                res = simulate_ball(probs)
                if(innings == 0):
                    allout = False
                    extra = False
                    runs1,wickets1,allout,extra = update_score(res, runs1, wickets1)
                    output = [innings, i, j, res, runs1, wickets1]
                    if(allout):
                        break
                    if(extra):
                        j -= 1


                if(innings == 1):
                    runs2,wickets2,allout,extra = update_score(res, runs2, wickets2)
                    output = [innings, i, j, res, runs2, wickets2]
                    if(allout):
                        break
                    if(extra):
                        j -= 1
                        pass
                j += 1
                #print(output)
            if(innings == 0 and wickets1 == 10):
                break
            if(innings == 1 and wickets2 == 10):
                break

    # print("----- End of Match -----")
    # print("Team 1 score: " + str(runs1) + "/" + str(wickets1))
    # print("Team 2 score: " + str(runs2) + "/" + str(wickets2))

    if(runs1 > runs2):
        return "Team 1 wins", runs1, wickets1, runs2, wickets2 
    elif(runs1 < runs2):
        return "Team 2 wins", runs1, wickets1, runs2, wickets2 
    else:
        return "Draw", runs1, wickets1, runs2, wickets2 




if __name__ == "__main__":
    probs = [3.03373168e+01, 3.69032605e+01, 6.38400149e+00, 3.18398908e-01,
             1.12773172e+01, 3.10128807e-02, 4.57388302e+00, 5.26702090e+00,
             4.90778837e+00]
    for i in range(1, len(probs)):
        probs[i] = probs[i] + probs[i-1]

    probs.insert(0, 0)

    runs = []
    wickets = []
    
    for i in range(10000):
        res, runs1, wickets1, runs2, wickets2 = simulate_game(probs)
        runs.append(runs1)
        runs.append(runs2)
        wickets.append(wickets1)
        wickets.append(wickets2)
    print("Average runs: " + str(sum(runs)/len(runs)))
    print("Average wickets: " + str(sum(wickets)/len(wickets)))

