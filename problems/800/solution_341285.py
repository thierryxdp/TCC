def total(compras,produtos):
    "Função que retorna a soma dos valores de um dicionário dado como entrada, os receber a lista com as palavras chaves. list, dict --> float"
    soma=0
    for insumo in compras:
        soma=soma+produtos[insumo]
    return round(soma,2)