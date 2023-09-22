def total(compra,preco):
    '''Essa função tem como objetivo calcular a soma dos itens(compra), caso eles
    constam no dicionario(preço)'''
    '''list,dict -> float'''
    i = 0
    soma = 0
    while i < len(compra):
        if compra[i] in preco:
            valor = dict.get(preco,compra[i])
            soma = soma + valor
        i+=1
    return round(soma,2)