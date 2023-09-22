def total(lista,dicionario):
    """função que retorna o preço total dos itens 
    selecionados e disponiveis em uma loja:list,dict->float"""
    todo:0
    for item in lista:
        if item in dicionario:
            todo+=dicionario[item]
    return todo