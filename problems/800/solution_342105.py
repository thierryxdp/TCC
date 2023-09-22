# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveil
def total(lista,dicionario):
    i=0
    p=0
    for produto in lista:
        if lista[i] in dicionario:
            p=p+dicionario[lista[p]]
            i=i+1
    return round(i,2)