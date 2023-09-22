# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista,produtos):
    result = 0
    for item in lista:
        if item in produtos:
            result+= produtos[item]
    return result