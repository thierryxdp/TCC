# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, produt):
    #estou criando uma variável para o preço da compra
    prec=0
    #somando os preços individuas da lista
    for produ in lista:
        prec+=produt[produ]
    preco=round(prec, 2)
    return preco