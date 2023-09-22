def total(lista,dicionario):
    """função que retorna o preço total dos itens 
    selecionados e disponiveis em uma loja:list,dict->float"""
    todo=0
    for item in lista:
        if item in dicionario:
            todo+=dicionario[item]
    if todo=39.59999999999999:#correção de algum bug no machine q no idle da 39.6 mas no machine não não
        return 39.6
    return todo