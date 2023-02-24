from cgi import test
import numpy as np
import time
import matplotlib.pyplot as plt
import csv
from csv import writer
import pandas as pd

class Match:
    teamA = "Team A"
    teamB = "Team B"
    #toss_outcome
    runs = [0,0,0,0]
    wickets = [0,0,0,0]
    total_runsB = 0
    total_runsA = 0
    iter = 10
    toss_winner = teamA
    data = [['batting_team', 'result','runs_scored', 'wickets_lost']]
    batting_team = ""
    file_name = "Four10_results.csv"


    probs = [2.98280285e+01, 3.71081235e+01, 6.52753241e+00, 3.19389965e-01,
       1.12894372e+01, 2.79466220e-02, 4.66409159e+00, 5.30686389e+00,
       4.92858640e+00]
    inning_number = 0

    def __init__(self):
        for i in range(1, len(self.probs)):
            self.probs[i] = self.probs[i] + self.probs[i-1]

        self.probs.insert(0, 0)

        c = np.random.uniform()*100
        if(c>50):
            self.toss_winner=self.teamB
        else:
            self.toss_winner=self.teamA
        self.batting_team = self.toss_winner

        # delimiter='\n'
        # header = ['Batting_team, Result, Runs, Wickets']
        # with open('Four10_results.csv', 'w', encoding='UTF8', newline='') as f:
        #     writer = csv.writer(f, delimiter=delimiter, quoting=csv.QUOTE_NONE, quotechar='',  lineterminator='\n')

        #     # write the header
        #     writer.writerow(header)
    
    '''
        Function to calculate extra runs scored when the ball bowled is an extra
    '''
    def calculate_extra_runs(self):
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

    '''
        Function to calculate extra runs scored when the ball bowled is an wicket
    '''
    def calculate_wicket_runs(self):
        wicket_probs = [89.1104006 ,  3.59225127,  0.16926838]
        for i in range(1, len(wicket_probs)):
            wicket_probs[i] = wicket_probs[i] + wicket_probs[i-1]

        wicket_probs.insert(0, 0)

        RV = np.random.uniform()*100
        for i in range(1, len(wicket_probs)):
            if(RV < wicket_probs[i] and RV >= wicket_probs[i-1]):
                return i
        return 0

    '''
        Function to simulate a ball bowled. The ball outcome is calculated using the prbabilities given.
        The function updates the runs and wickets
    '''
    def simulate_ball(self):
        RV = np.random.uniform()*100
        for i in range(1, len(self.probs)):
            if(RV < self.probs[i] and RV >= self.probs[i-1]):
                res = i-1
        
        #result = ''
        if(res == 0):
            result = 'dot'
        elif(res == 1):
            result =  'one'
            self.runs[self.inning_number] += 1
        elif(res == 2):
            result =  'two'
            self.runs[self.inning_number] += 2
        elif(res == 3):
            result =  'three'
            self.runs[self.inning_number] += 3
        elif(res == 4):
            result =  'four'
            self.runs[self.inning_number] += 4
        elif(res == 5):
            result =  'five'
            self.runs[self.inning_number] += 5
        elif(res == 6):
            result =  'six'
            self.runs[self.inning_number] += 6
        elif(res == 7):
            result =  'extra run'
            self.runs[self.inning_number] += self.calculate_extra_runs()
        elif(res == 8):
            result =  'wicket'
            self.runs[self.inning_number] += self.calculate_wicket_runs()
            self.wickets[self.inning_number] +=1
        else:
            result = ''
            #print(RV)
        
        return result

    def batting_innings(self):
        # wickets = 0
        # runs = 0
        for o in range(1,11):
            for b in range(1,7):
                if(self.inning_number == 3):
                    if(self.runs[1] + self.runs[3]>self.runs[0]+self.runs[2]):
                        break
                if(self.wickets[self.inning_number]==10):
                    break
                res = self.simulate_ball()
                #print(self.batting_team, res, self.runs[self.inning_number], self.wickets[self.inning_number])
                self.data.append([self.batting_team, res, self.runs[self.inning_number], self.wickets[self.inning_number]])
                #print(res + str(runs) + str(wickets))
                if(res == "extra run"):
                    b -= 1
                #print("" + str(o) + ":" + str(b) + ":" + str(res))
            if(self.wickets[self.inning_number] == 10):
                break
    
    
    def play_game(self):
        
        while(self.inning_number<4):
            #print(self.batting_team)
            self.batting_innings()
            self.inning_number = self.inning_number+1
            if(self.batting_team==self.teamA):
                self.batting_team = self.teamB
            else:
                self.batting_team=self.teamA
        # print(c)
        print(self.runs)
        print(self.wickets)

        if(self.toss_winner==self.teamB):
            self.total_runsB = self.runs[0] + self.runs[2]
            self.total_runsA = self.runs[1] + self.runs[3]
        else:
            self.total_runsA = self.runs[0] + self.runs[2]
            self.total_runsB = self.runs[1] + self.runs[3]

        
        df = pd.DataFrame(self.data, columns=["ball #", "batting team", "runs scored", "wickets lost"])
        df.columns=["ball #", "batting team", "runs scored", "wickets lost"]
        df.to_csv(self.file_name, header=False)
        
        # delimiter='\n'
        # with open(self.file_name, 'w', encoding='UTF8', newline='') as f:
        #     writer = csv.writer(f)

        #     # write the header
        #     self.data
        #     writer.writerow(self.data)

        
        
        
        
    
    def restart(self):
        self.runs = [0,0,0,0]
        self.wickets = [0,0,0,0]
        self.total_runsB = 0
        self.total_runsA = 0
        self.inning_number=0

        c = np.random.uniform()*100
        if(c>50):
            self.toss_winner=self.teamB
        else:
            self.toss_winner=self.teamA
        self.batting_team = self.toss_winner

        self.data = [['batting_team', 'result', 'runs_scored', 'wickets_lost']]

        
        
    
    def test_func(self):
        runs = []
        team1_wins = 0
        team2_wins = 0
        run_margins = []
        wicket_margins = []
    
        for i in range(self.iter):
            print("Game No: " + str(i+1))
            self.file_name = "Four10_results" + str(i+1) + ".csv"
            self.play_game()
            runs.append(self.total_runsA)
            runs.append(self.total_runsB)
            if(self.toss_winner == self.teamA):
                if(self.total_runsA>self.total_runsB):
                    team1_wins += 1
                    run_margins.append(self.total_runsA-self.total_runsB)
                    print(self.teamA + " wins by " + str(run_margins[-1]) + " runs")
                elif(self.total_runsB>self.total_runsA):
                    team2_wins += 1
                    wicket_margins.append(10-self.wickets[3])
                    print(self.teamB + " wins by " + str(wicket_margins[-1]) + " wickets")
            else:
                if(self.total_runsA>self.total_runsB):
                    team1_wins += 1
                    wicket_margins.append(10-self.wickets[3])
                    print(self.teamA + " wins by " + str(wicket_margins[-1]) + " wickets")
                elif(self.total_runsB>self.total_runsA):
                    team2_wins += 1
                    run_margins.append(self.total_runsB-self.total_runsA)
                    print(self.teamB + " wins by " + str(run_margins[-1]) + " runs")
            
            self.restart()
        # return sum(runs)/len(runs), team1_wins*100/iter, team2_wins*100/iter, run_margins, wicket_margins
        return sum(runs)/len(runs), team1_wins, team2_wins, run_margins, wicket_margins
    

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


m = Match()
res = m.test_func()
#print(m.probs)
# for i in range(100):
#     print(m.simulate_ball())
# #print(m.data)
print((res[0], res[1], res[2]))
#margins_plot(res[3], res[4])


