# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(l, d):
    """Recebe como parâmetro uma lista de compras em que cada elemento é uma string representando um produto e um dicionário em que cada chave é o produto disponível na loja e o seu respectivo valor é o preço do produto. Retorna o valor total dos itens da lista que estejam disponíveis na loja arredondado para duas casa decimais;
    assinatura: list, dict --> float
    Casos de teste:
    total(['manteiga', 'arroz'], {'chocolate': 3, 'manteiga': 5, 'arroz': 2.50}) == 7.5
    total(['feijão', 'leite', 'macarrâo'], {'detergente': 1.99, 'macarrão': 4.50, 'feijão': 7.99, 'leite': 4.59}) == 12.58
    """
    v = 0
    for item in l:
        if item in d:
            v += d[item]
    return round(v, 2)