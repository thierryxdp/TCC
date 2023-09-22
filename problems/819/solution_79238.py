def mmc(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto is not 0:
        resto = a % b
        a  = b
        b  = resto

    return (num1 * num2) / a

def filtraMultiplos(lista,n):
    '''função que que filtra os multiplos de n da lista, list,int->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]% mmc(lista[i],n)==0:
            multiplos=multiplos+lista[i]
        i=i+1
    return multiplos