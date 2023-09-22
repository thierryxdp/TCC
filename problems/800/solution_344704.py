# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista, produt):
    prec=0
    for produ in lista:
        prec+=produt[produ]
    preco=round(prec, 2)
    return preco