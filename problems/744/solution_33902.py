from math import*

def hashtag(s):
    '''Funcao que adiciona (#) no inicio, no meio e no final de uma saida, dadas as entradas
str-> str'''

    a= len (s)/2
    b= len (s)%2
    c= term (a)
    
    if (b==0):
        return '#' + s[0:c] + s[c:]+ '#'
    elif (b==1):
        return '#' +s[0:c] + '#' + s[c:] + '#'