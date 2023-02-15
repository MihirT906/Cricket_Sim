from cgi import test
import numpy as np
import time
import matplotlib.pyplot as plt

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
    for o in range(1,11):
        for b in range(1,7):
            if(wickets==10):
                break
            res,runs, wickets = simulate_ball(probs, runs, wickets)
            if(res == "extra run"):
                b -= 1
            #print("" + str(o) + ":" + str(b) + ":" + str(res))
        if(wickets == 10):
            break
        
    return runs, wickets





def simulate_game(probs1, probs2):
    runs1A = 0
    wickets1A = 0
    runs2A = 0
    wickets2A = 0
    runs1B = 0
    wickets1B = 0
    runs2B = 0
    wickets2B = 0

    c = np.random.uniform()*100
    #print(c)
    if(c>50):
        runs1B, wickets1B = simulate_innings(probs2)
        runs1A, wickets1A = simulate_innings(probs1)
        runs2B, wickets2B = simulate_innings(probs2)
        runs2A, wickets2B = simulate_innings(probs1)

    else:
        
        runs1A, wickets1A = simulate_innings(probs1)
        runs1B, wickets1B = simulate_innings(probs2)
        runs2A, wickets2B = simulate_innings(probs1)
        runs2B, wickets2B = simulate_innings(probs2)

    runsA = runs1A + runs2A
    runsB = runs1B + runs2B
    winMargin = abs(runsA-runsB)
    # runs1, wickets1 = simulate_innings(probs1)
    # runs2, wickets2 = simulate_innings(probs2)

    # # print("----- End of Match -----")
    # # print("Team 1 score: " + str(runs1) + "/" + str(wickets1))
    # # print("Team 2 score: " + str(runs2) + "/" + str(wickets2))

    if(runsA > runsB):
        return "Team 1 wins", runsA, runsB, winMargin
    elif(runsA < runsB):
        return "Team 2 wins", runsA, runsB, winMargin
    else:
        return "Draw",  runsA, runsB, winMargin  

def test_func(probs1, probs2, iter):
    runs = []
    wickets = []
    team1_wins = 0
    team2_wins = 0
    win_margins = []
    
    for i in range(iter):
        res, runs1, runs2, wm = simulate_game(probs1, probs2)
        runs.append(runs1)
        runs.append(runs2)
        win_margins.append(wm)
        # wickets.append(wickets1)
        # wickets.append(wickets2)
        if(res == "Team 1 wins"):
            team1_wins += 1
        elif(res == "Team 2 wins"):
            team2_wins += 1
        #print(res)
    
    return sum(runs)/len(runs), team1_wins*100/iter, team2_wins*100/iter, win_margins


def wm_plot(win_margins):
    counts, edges, bars = plt.hist(win_margins)
    plt.xlabel("Win Margin")
    plt.ylabel("Frequency")
    plt.title("Histogram of Win Margin")
    #bar_labels = bars/len(win_margins)
    plt.bar_label(bars)
    plt.show()
    

if __name__ == "__main__":
    probs1 = [2.98280285e+01, 3.71081235e+01, 6.52753241e+00, 3.19389965e-01,
       1.12894372e+01, 2.79466220e-02, 4.66409159e+00, 5.30686389e+00,
       4.92858640e+00]
    probs2 = [2.98280285e+01, 3.71081235e+01, 6.52753241e+00, 3.19389965e-01,
       1.12894372e+01, 2.79466220e-02, 4.66409159e+00, 5.30686389e+00,
       4.92858640e+00]
    for i in range(1, len(probs1)):
        probs1[i] = probs1[i] + probs1[i-1]
        probs2[i] = probs2[i] + probs2[i-1]

    probs1.insert(0, 0)
    probs2.insert(0, 0)
    
    avg_runs, team1_w_p, team2_w_p, win_margins = test_func(probs1,probs2,10000)

    print("Average runs: " + str(avg_runs))
    #print("Average wickets: " + str(avg_wickets))
    print("% won by team 1: " + str(team1_w_p) + "%")
    print("% won by team 2: " + str(team2_w_p) + "%")

    wm_plot(win_margins)



