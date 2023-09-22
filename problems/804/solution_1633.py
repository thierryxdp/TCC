#Start your python function here
def filtra_pares(a,b,c,d):
    para= a%2
    parb= b%2
    parc= c%2
    pard= d%2
    par= (a)
    par1= (a,b,c,d)
    par2=( a,b,c)
    par3= (a,b)
    par4= (a,c)
    
    if (para==0 and parb==0 and parc==0 and pard==0):
        return (par1)
    elif (para!=0 and parb==0 and parc==parb and pard==parb):
        return ()