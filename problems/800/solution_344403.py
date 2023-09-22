# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas 
def total(lista_compras, dicionario):
    """ dado uma lsta de compras e um dicionário contendo o valor de cada item, retorna o valor total das compras.
    entrada string e dicionário -> saida float. """
    
    total = 0
    
    for proximo in lista_compras:
        if proximo in dicionario:
            total = total + dicionario[proximo]
    return round(total,2)