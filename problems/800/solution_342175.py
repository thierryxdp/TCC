def total(ls, tabela):
    """Função que retorna o valor total dos produtos de uma loja dado uma lista contendo os valores dos produtos de uma loja, tal como o nome dos produtos. Entrada -> Str; Saída -> dict """
    custo = 0
    for p in ls:
        custo += dict.get(tabela, p, 0)
    return round(custo, 2)