# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef total(lista_de_compras,produtos):
    soma=0
    for produto in lista_de_compras:
        preco_item=produtos[produto]
        soma+=preco_item
    return round(soma,2)