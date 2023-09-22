# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras,produtos):
    ''' 
    Recebe uma lista de compras e um dicionário contendo os preços de cada produto
    Retorna o valor total dos itens da lista que estejam disponiveis na loja.
    '''
    valor=[]
    for k in lista_compras:
        if k in produtos:
            valor.append(produtos[k])
    return round(sum(valor),2)