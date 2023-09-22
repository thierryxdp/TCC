def total(lista,produtos):
    '''A funçaõ recebe uma lista em um dicionario e retorna 
    o valor total dos itens valores do dicionario.
    list,dict->int'''
    
    soma=0.00
    indice=0
    while indice<len(lista):
        a=produtos[lista[i]]
        soma=soma+a
        indice=indice+1
    soma=round(soma,2)
    return soma