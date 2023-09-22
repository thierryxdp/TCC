def filtra_pares(a,b,c,d):
 A=[]
 B=[]
 C=[]
 D=[]
 lista=[a,b,c,d]
   if a % 2 == 0:
        A=[a]
    if b % 2 == 0:
        B=[b]
    if c % 2 == 0:
         C=[c]
    if a % 2 == 0:
        D=[d]
    return A+B+C+D