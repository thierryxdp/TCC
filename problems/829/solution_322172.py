def soma_h(n):
    '''calcula o valor de H com n termos onde n é inteiro e o resultado tem apenas
    2 casas decimais'''
    h = 0
    for i in range(1, n+1):
        h = h + (1/i)
    casas = round(h, 2)
    return casas