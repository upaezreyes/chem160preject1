from random import random,choice
from math import exp

n1 = 20                         # sites per edge for nxn system
n3 = n1*n1*n1                  # preculculate n*n*n
nlist = list(range(n1))        # list of sites
ntrials = 200000               # number of trials
nequil = 100000                # equilibration steps
Tmax = 7.0    # max temperature
Temp = 0.1
dT = 0.1      # change of temperature

#Calculate Cv and Ev at a temperature range from 0 to 7
while Temp<Tmax:
    Temp += dT
    E_sum = 0.0
    E2_sum = 0.0

    #matrix of spins all spin up
    spins = [[[1 for u in range(n1)] for v in range(n1)] for t in range(n1)]

    # run simulation
    for trial in range(1,(ntrials+nequil+1)):
        # randomly pick a site
        u = choice(nlist)
        v = choice(nlist)
        t = choice(nlist)
        #Calculate the change in energy if we flit this spin
        deltaE = 2.*(spins[u][v][t]*\
                              (spins[u][(v+1)%n1][t]+spins[u][(v-1+n1)%n1][t]+\
                              spins[(u+1)%n1][v][t]+spins[(u+n1-1)%n1][v][t] +\
                              spins[u][v][(t+1)%n1]+spins[u][v][(t+n1-1)%n1]))
    
        #Flip the spin using Metropolis MC
        if exp(-deltaE/Temp)>random():
            spins[u][v][t] = - spins[u][v][t]
        else:
            deltaE = 0.0
        #Calculate system energy ONCE
        if trial == nequil:
            energy2 = 0.0
            for i in range(n1):
                for j in range(n1):
                     for z in range(n1):
                         energy2 -=(spins[u][v][t]*\
                              (spins[u][(v+1)%n1][t]+spins[u][(v-1+n1)%n1][t]+\
                              spins[(u+1)%n1][v][t]+spins[(u+n1-1)%n1][v][t] +\
                              spins[u][v][(t+1)%n1]+spins[u][v][(t+n1-1)%n1]))
            energy2/=n3
    
        # update energy based on deltaE per spin
        if trial > nequil:
            energy2 += 2*deltaE/n3
            E_sum += energy2
            E2_sum += energy2*energy2
                     
    E_ave = E_sum/ntrials
    E2_ave = E2_sum/ntrials
    Cv = 1./(Temp**2)*(E2_ave-E_ave*E_ave)
    print("%8.4f %10.6f %10.6f"%(Temp, E_ave, Cv))
    







               
        

