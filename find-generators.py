# Find generators of Zn*
n = 23456471
divisors_of_phi = [1,2,5,10,229,458,1145,2290,10243,20486,51215,102430,2345647,4691294,11728235] # except phi(n)=23456470
generators = []
for g in range(1,n):
    check = True
    if len(generators)==10:
        break
    else:
        for div in divisors_of_phi:
            if pow(g,div,n) == 1:
                check = False
        if check != False:
            generators.append(g)
print(generators)
