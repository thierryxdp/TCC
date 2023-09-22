def total(compras,preço):

    soma = 0

    for dado in compras:

        if dado in preço:

            soma = soma + preço[dado]

    return soma