#Questao 1
def filtraMultiplos(l,n):
    '''Funcao que filtra os multiplos de um numero n.list,int -> list'''
    x=0
    while x<len(l):
        if l[x]%n!=0:
            l.pop(x)
        else:
            x=x+1
    return l