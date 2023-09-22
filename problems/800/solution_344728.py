# Total
def total(lista,tabela):
    """Esta função recebe uma lista de itens e uma tabela de precos referentes aos itens e soma os valores
    list -> int"""
    lista = list(lista)
    total = 0
    for i in range(len(lista)):
        total = total + (tabela[lista[i]])
    return round(total,2)# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis