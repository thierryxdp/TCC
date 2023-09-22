def total(compras,preco):

    soma = 0

    for dado in compras:

        if dado in preco:

            soma = soma + preco[dado]

    return round(soma,3)