# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveil
def total(lista,dicionario):
    i=0
    for produto in lista:
        if lista[i] in dicionario:
            i=i+dicionario[lista[i]]
    return round(i,2)