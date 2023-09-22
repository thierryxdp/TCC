def filtraMultiplos(li,num):
    '''Recebe uma lista e um inteiro e 
    retorna uma outra lista que é a 
    divisão do elemento da lista por inteiro
    que dessem como resultado 0
    list,int->list'''
    filtrados=[]
    i=0
    while i<len(li):
        if li[i]%num==0:
        	filtrados=filtrados+[li[i]]
        i=i+1
    return filtrados