def total(lista,dic):
    """Função que recebe uma lista de compras e um dicionário contendos os itens e seus preços disponíveis na loja. Retorna o valor total a ser gasto"""
    """str,dic--->float"""
    valor_total=0
    v=0
    i=0
    while i<len(lista):
        if lista[i] in list(dict.keys(dic)):
            v+=dict.get(dic,lista[i])
        i+=1
    valor_total= round(v,2)