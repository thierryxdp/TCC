def total (lista_de_compra, dicionario):
    soma = 0 
    for produto in dicionario:
        if dicionario in lista_de_compra[produto]:
            soma = soma + produto
    return round(soma, 2)