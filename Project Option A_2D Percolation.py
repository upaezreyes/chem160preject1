from random import choice

npart=500   
side=41  #Should be an odd number
#time=0
density = choice((0,1))
#a = input(density)
maxsteps = 1000  # max number of steps the particle can move out of the grid
perc = 0   # initialize to zero which will count the number of times the partile
           # Sucessfully move from the center to an edge

steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]

for ipart in range(npart):
    # Start particle at center
    x,y = side//2,side//2
    #counter=0
    for x in range(side):
        x = density
        
        for y in range(side):
            y = density
    # perform the random walk until particle departs
    for isteps in range(maxsteps):
       # counter+=1
        grid[x][y]=0.0  #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x ==1 or y ==1:
            continue
        
        if x<0 or y<0 or x==side or y==side:
            #time+=counter
            perc += 1 
            break
        grid[x][y]=1   #Put particle in new location
#avetime=time/npart
print("Probability of the particle percolating out of the system =%5.2f"%(perc/npart))

