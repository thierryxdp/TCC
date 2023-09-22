def repetidos(lista):
    """Função que recebe uma lista de numeros e retorna o numero de vezes que algum elemento da lista é igual ao elemento anterior
    list --> int"""
    i=0
    novalista=[]
    while i<len(lista)-1:
        if lista[i] == lista[i+1]:
            list.append(novalista, True)
        else:
            list.append(novalista, False)
        i+=1
    return novalista.count(True)