def filtraMultiplos(t,n):
    '''funcao que filtra os multiplos de um numero inteiro n presentes em uma lista t
    tuple,int->tuple'''
    multiplos=()
    proximo=0
    while proximo<len(t):
        if t[proximo]%n==0:
            multiplos=multiplos+(t[proximo],)
        proximo=proximo+1
    return multiplos