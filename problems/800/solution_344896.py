# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis 
def total(lista, dicionario):
    total = 0
    for produto in lista:
        total += produto 
    return round(total,2)