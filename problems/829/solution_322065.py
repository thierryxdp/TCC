def soma_h(termos):
    '''calcula e retorna o valor H com N termos
    retornando a sua soma
    int -> float'''
    valores = []
    for i in range(1,termos+1):
        valores += (1/i)
    return round(sum(valores),2)