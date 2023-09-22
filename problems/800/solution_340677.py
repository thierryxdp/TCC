def total (lista,dicio):
    i = 0
    compras = 0 

    for n in lista:
        if lista[i] in dict.keys(dicio):
            compras = compras + dict.get(dicio,lista[i])
            i = i + 1
        elif lista[i] in dict.keys(dicio):
            compras = compras
            i = i + 1
    return round.compras
    
    # Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis