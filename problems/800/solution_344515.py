def total(lista,produtos):
    """ Função que retorna o valor total dos itens da lista. Input str, dict. Return float  """

    resposta = 0
    
    for i in lista:
        if i in produtos:
            resposta = resposta + produtos[i]
 	return round(resposta,2)