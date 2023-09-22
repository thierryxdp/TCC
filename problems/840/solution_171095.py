from math import ceil

def bolos(a,b,c):
    '''A funcao retorna a quantidade de bolos que podem 
ser feitos com as quantidads a, b e c de ingredientes
sabendo que so serao feitos bolos com o minimo de 
ingredientes 2,3 e 5 respectivamente'''
    if min(a,b,c)==a and (b>=(a/2)*3) and (c>=(a/2)*5):
        return a/2 
    if min(a,b,c)==b and (a>=(b/3)*2) and (c>=(b/3)*5):
        return b/3
    if min(a,b,c)==c and (a>=(c/5)*2) and (b>=(c/5)*3):
        return c/5
        if (a<2)or(b<3)or(c<5):
        return 0
    else:
        return ceil(((a+b+c)/10)-1)