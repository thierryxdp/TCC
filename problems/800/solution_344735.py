def total(lista,tabela):
    """Esta função recebe a lista de itens e uma tabela de precos destinados aos itens e soma os valores
    list -> int"""
    lista = list(lista)
    total = 0
    for i in range(len(lista)):
        total = total + (tabela[lista[i]])
    return round(total,2)