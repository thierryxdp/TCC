# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras,produtos):
    '''função que retorna o valor total da lista de compras
    [], {} --> float'''
    preco_total = 0
    for i in range(len(lista_compras)):
        if lista_compras[i] in produtos:
            preco_total = preco_total + produtos[lista_compras[i]]
    return round(preco_total, 2)