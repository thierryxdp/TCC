# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_de_compras, produtos):
        #lista de compras e um dicionário contendo o preço de cada produto disponível. retornando o total to valor dos itens listados
        #entrada lista_de_compras: tupla ; produtos: dicionario ; saida: total com 2 digitos na decimal   
    total = 0
    for item in lista_de_compras:
        if item in produtos.keys():
            total += produtos[item]
    return round(total, 2)