# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras, produto):
    '''
        recebe uma lista de compra e retorna o valos total dos produtos dessa
        lista, disponiveis em um supermercado, produtos que devem constar em
        um dicionario recebido como parametro juntamente com a lista de compras
        entrada: lista, dicionario
        saida: float
    '''
    valor_final = 0
    for chq in range(len(lista_de_compras)):
        if lista_de_compras[chq] in dict.keys(produto):
            valor_final = round(valor_final, 2) + round(produto[lista_de_compras[chq]], 2)
    return valor_final