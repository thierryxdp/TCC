def filtraMultiplos (lista,n):
    '''primeiro usando o whilw para contar a lista e ver quando seu 
    resto for 0 e usando o append para adicionar o resultado
    no final da lista'''
    resposta=[]
    i=0
    while i < len(lista):
        if lista[i]%n==0:
            resposta.append(lista[i])
        i+=1
    return resposta