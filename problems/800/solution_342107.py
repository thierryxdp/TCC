# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveil
def total(lista,dicionario):
    i=0
    for produto in dicionario:
        if produto in lista:
            i=i+dicionario[produto]
    return range(i,2)