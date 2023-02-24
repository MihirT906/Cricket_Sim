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



def batting_innings(probs):
    wickets = 0
    runs = 0
    for o in range(1,11):
        for b in range(1,7):
            if(wickets==10):
                break
            res,runs, wickets = simulate_ball(probs, runs, wickets)
            #print(res + str(runs) + str(wickets))
            if(res == "extra run"):
                b -= 1
            #print("" + str(o) + ":" + str(b) + ":" + str(res))
        if(wickets == 10):
            break
        
    return runs, wickets

def chasing_innings(probs, target_score):
    wickets = 0
    runs = 0
    for o in range(1,11):
        for b in range(1,7):
            if(runs>=target_score):
                break
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
        toss_winner = "B"
        runs1B, wickets1B = batting_innings(probs2)
        runs1A, wickets1A = chasing_innings(probs1, runs1B)
        runs2B, wickets2A = batting_innings(probs2)
        runs2A, wickets2B = chasing_innings(probs1, runs2B)

    else:
        toss_winner = "A"
        runs1A, wickets1A = batting_innings(probs1)
        runs1B, wickets1B = chasing_innings(probs2, runs1A)
        runs2A, wickets2A = batting_innings(probs1)
        runs2B, wickets2B = chasing_innings(probs2, runs2A)

    runsA = runs1A + runs2A
    runsB = runs1B + runs2B
    wicketsA = 10-wickets2A
    wicketsB = 10-wickets2B
    #winMargin = abs(runsA-runsB)
    # runs1, wickets1 = simulate_innings(probs1)
    # runs2, wickets2 = simulate_innings(probs2)

    # print("----- End of Match -----")
    # print("Team 1 score: " + str(runs1A) + "/" + str(wicketsA))
    # print("Team 2 score: " + str(runs1B) + "/" + str(wicketsB))
    # print("Team 1 score: " + str(runs2A) + "/" + str(wicketsA))
    # print("Team 2 score: " + str(runs2B) + "/" + str(wicketsB))
    # print(wicketsA)
    # print(wicketsB)

    if(runsA > runsB):
        return "Team A wins", runsA, runsB, wicketsA, wicketsB, toss_winner
    elif(runsA < runsB):
        return "Team B wins", runsA, runsB, wicketsA, wicketsB, toss_winner
    else:
        return "Draw",  runsA, runsB, wicketsA, wicketsB, toss_winner

def test_func(probs1, probs2, iter):
    runs = []
    team1_wins = 0
    team2_wins = 0
    run_margins = []
    wicket_margins = []
    
    for i in range(iter):
        res, runsA, runsB, wicketsA, wicketsB, toss_winner = simulate_game(probs1, probs2)
        runs.append(runsA)
        runs.append(runsB)
        if(toss_winner == "A"):
            if(res == "Team A wins"):
                team1_wins += 1
                run_margins.append(runsA-runsB)
            elif(res == "Team B wins"):
                team2_wins += 1
                wicket_margins.append(wicketsB)
        else:
            if(res == "Team A wins"):
                team1_wins += 1
                wicket_margins.append(wicketsA)
            elif(res == "Team B wins"):
                team2_wins += 1
                run_margins.append(runsB-runsA)
    
    return sum(runs)/len(runs), team1_wins*100/iter, team2_wins*100/iter, run_margins, wicket_margins


def margins_plot(run_margins, wicket_margins):
    plt.figure()
    # plt.hist(run_margins)
    # plt.show()
    plt.subplot(121)
    counts, edges, bars = plt.hist(run_margins, bins=10, edgecolor='black', align="mid")
    # ticks = [(patch._x0 + patch._x1)/2 for patch in bars]
    # ticklabels = [i for i in range(10)]
    plt.xlabel("Run Margin")
    plt.ylabel("Frequency")
    plt.title("Histogram of Run Margins")
    #bar_labels = bars/len(win_margins)
    plt.bar_label(bars)
    # plt.show()

    plt.subplot(122)
    labels, counts = np.unique(wicket_margins, return_counts=True)
    fig = plt.bar(labels, counts, align='center', color = "orange")
    plt.gca().set_xticks(labels)
    for p in fig:
        height = p.get_height()
        plt.annotate('{}'.format(height),
            xy=(p.get_x() + p.get_width() / 2, height),
            xytext=(0, 3), # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')
    #fig.bar_label(fig.containers[0], label_type='edge')
    plt.xlabel("Wicket Margin")
    plt.ylabel("Frequency")
    plt.title("Histogram of Wicket Margins")
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
    
    avg_runs, team1_w_p, team2_w_p, run_margins, wicket_margins = test_func(probs1,probs2,1)

    print("Average runs: " + str(avg_runs))
    #print("Average wickets: " + str(avg_wickets))
    print("% won by team 1: " + str(team1_w_p) + "%")
    print("% won by team 2: " + str(team2_w_p) + "%")

    # print(len(run_margins))
    # print(len(wicket_margins))
    margins_plot(run_margins, wicket_margins)



