from math import*
def hashtag(s):
    '''Funcao que adiciona (#) no inicio, no meio e no final de uma saida, dadas as entradas
str-> str'''

    x= len (s)/2
    y= len (s)%2
    z= floor (x)
    
    if (y==0):
        return '#' + s[0:z] + '#'+ s[z:]+ '#'
    
    elif (y==1):
        return '#' +s[0:z] + '#' + s[z:] + '#'