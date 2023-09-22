def filtraMultiplos(lista_num,num):
    '''funcao que dada uma lista de numeros e um numero, retorna uma nova lista que contem somente os multiplos do numero;
       list,int->list'''
    multiplos=[]
    outra_lista=multiplos.copy
    i=0
    while i<len(lista_num):
        if lista_num[i]%num==0:
            outra_lista= multiplos.append(lista_num[i])
        i=i+1
    return multiplos