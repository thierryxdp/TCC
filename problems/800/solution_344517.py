def total(lista,produtos):
    """ Função que retorna o valor total dos itens da lista. Input str, dict. Return float  """

    x = 0
    
    for i in lista:
        if i in produtos:
            x = x + produtos[i]

    resposta = round(x,2)
    
    return resposta