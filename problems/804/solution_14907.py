# Função que filtra os números pares inteiros de uma tupla
#tupla->tupola
#a,b,c, d são números inteiros quaisquer 
def filtra_pares(a,b,c,d):
    if a/2==0 and b/2==0 and c/2==0 and d/2==0:
        return (a,b,c,d)
    elif a/2!=0 and b/2==0 and c/2==0 and d//2==0:
        return (b,c,d)
    elif a/2==0 and b/2!=0 and c/2==0 and d/2==0:
        return (a,c,d)
    elif a/2==0 and b/2==0 and c/2!=0 and d/2==0:
        return (a,b,d)
    elif a/2==0 and b/2==0 and c/==0 and d/2!=0:
        return(a,b,c)