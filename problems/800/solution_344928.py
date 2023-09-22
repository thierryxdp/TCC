# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,preco):
    precos=0
    for item in lista:
        precos=precos+preco(item)
    return precos