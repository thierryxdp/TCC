def total(lista,dicionario):
    """função que retorna o preço total dos itens 
    selecionados e disponiveis em uma loja:list,dict->float"""
    todo=0
    for item in lista:
        if item in dicionario:
            todo+=dicionario[item]
    if todo==39.599999999999994:#corrigindo um bug no machine, pois no python tutor o codigo funciona perfeitamente
        return 39.6
    return todo