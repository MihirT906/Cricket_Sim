import numpy as np

runs1 = 0
wickets1 = 0
runs2 = 0
wickets2 = 0
for innings in range(2):
    for i in range(20):
        for j in range(6):
            outcome = np.random.uniform()
            if(outcome<1/11 and outcome>=0):
                result = 'dot'
            elif(outcome<2/11 and outcome>=1/11):
                result = 'one'
            elif(outcome<3/11 and outcome>=2/11):
                result = 'two'
            elif(outcome<4/11 and outcome>=3/11):
                result = 'three'
            elif(outcome<5/11 and outcome>=4/11):
                result = 'four'
            elif(outcome<6/11 and outcome>=5/11):
                result = 'five'
            elif(outcome<7/11 and outcome>=6/11):
                result = 'six'
            elif(outcome<8/11 and outcome>=7/11):
                result = 'by'
            elif(outcome<9/11 and outcome>=8/11):
                result = 'wide'
            elif(outcome<10/11 and outcome>=9/11):
                result = 'no_ball'
            elif(outcome<1 and outcome>=10/11):
                result = 'wicket'
            
            if(innings == 0):
               
                if(result == 'dot'):
                    pass
                elif(result == 'one'):
                    runs1+=1
                elif(result == 'two'):
                    runs1 +=2
                elif(result == 'three'):
                    runs1+=3
                elif(result == 'four'):
                    runs1+=4
                elif(result == 'five'):
                    runs1+=5
                elif(result == 'six'):
                    runs1 +=6
                elif(result == 'wide'):
                    runs1+=1
                    j-=1
                elif(result == 'no_ball'):
                    runs1+=1
                    j-=1
                    #Next ball feature
                elif(result == 'wicket'):
                    wickets1+=1
                    if(wickets1 == 10):
                        print("Break from wickets 1")
                        break
            

            if(innings == 1):
                if(result == 'dot'):
                    pass
                elif(result == 'one'):
                    runs2+=1
                elif(result == 'two'):
                    runs2 +=2
                elif(result == 'three'):
                    runs2+=3
                elif(result == 'four'):
                    runs2+=4
                elif(result == 'five'):
                    runs2+=5
                elif(result == 'six'):
                    runs2 +=6
                elif(result == 'wide'):
                    runs2+=1
                    j-=1
                elif(result == 'no_ball'):
                    runs2+=1
                    j-=1
                    #Next ball feature
                elif(result == 'wicket'):
                    wickets2+=1
                    if(wickets2 == 10):
                        break
                    
        if(innings == 0 and wickets1 == 10):
            break
        if(innings == 1 and wickets2 == 10):
            break
            
            


print(runs1)
print(wickets1)
print(runs2)
print(wickets2)

if(runs1>runs2):
    print("Team 1 wins")
elif(runs1<runs2):
    print("Team 2 wins")
else:
    print("Draw")
