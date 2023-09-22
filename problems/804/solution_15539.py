#Start your python function herepar=[]
conjunto=[]

def numero(par, conjunto):
    for x in conjunto:
        if x%2==0:
            par.append(x)
        
    print("conjunto lido:", conjunto)
    print("conjunto dos pares:", par)
    
    return (x)
i=0
for i in range (1,5,1):
    
    x= int(input())
    conjunto.append(x)

numero(par, conjunto)