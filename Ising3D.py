from random import choice

n=8
# Initialize all spin up (+1) case
spins=[[[1 for i in range(n)] for j in range(n)] for z in range(n)]
# Calculate the system energy
energy1=0
for i in range(n):
    for j in range(n):
        for z in range(n):
            energy1 -=(spins[i][j][z]*(spins[i][(j+1)%n][z]+spins[i][(j-1+n)%n][z]+\
                              spins[(i+1)%n][j][z]+spins[(i+n-1)%n][j][z] +\
                              spins[i][j][(z+1)%n]+spins[i][j][(z+n-1)%n]))
        
print("<E>=%4.2f"%(float(energy1)/(n*n*n)))

# Initialize random spin (+1 or -1) case 
spins=[[[choice((-1,1)) for x in range(n)] for y in range(n)] for z in range(n)] 

# Calculate the system energy 
energy=0
for i in range(n):
    for j in range(n):
        for z in range(n):
            energy-=(spins[i][j][z]*(spins[i][(j+1)%n][z]+spins[i][(j-1+n)%n][z]+\
                              spins[(i+1)%n][j][z]+spins[(i+n-1)%n][j][z] +\
                              spins[i][j][(z+1)%n]+spins[i][j][(z+n-1)%n]))

print("<E>=%4.2f"%(float(energy)/(n*n*n)))

#Print out ising model
sym =["+","-"]
for i in range(n):
    for j in range(n):
        for z in range(n):
                 print("%s"%(sym[(spins[i][j][z]+1)//2]),end=" ")
    print("")


