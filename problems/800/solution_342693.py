# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lista_compras, dict_precos):
    ''' Retorna o valor total de uma dada lista de compras
    list, dict -> int'''
    
    total_compras = 0
    for i in range(len(lista_compras)):
        total_compras += dict_precos[lista_compras[i]]
        
    return round(total_compras, 2)