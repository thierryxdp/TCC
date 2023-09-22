#Start your python function here
def filtra_pares(a,b,c,d):
    para= a%2
    parb= b%2
    parc= c%2
    pard= d%2
    if (para==0 and parb==0 and parc==0 and pard==0):
        return (a,b,c,d)