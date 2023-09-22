def total(lista_de_compras,precos):
    ''' recebe uma lista de compras e os preços dos produtos que disponiveis em uma loja e
    retorna a soma dos preços dos produtos disponiveis na loja que estão na lista de compras'''
    valor = []
    valores_totais=[]
    for i in lista_de_compras:
        if i in precos:
            x= precos['i']
            list.append(valores_totais,x)
    return sum(valores_totais)