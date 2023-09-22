def primo(n):
    '''Dado um número positivo inteiro n, verifica se este número é primo
    int->bool'''
x=0    
for i in range(1,n+1):
    if n%i==0:
        x=x+1
        
if x==2:
    return True
else:
    return False