def total(lista:str,preco:dict)->float:
    '''calcula o valor total dos produtos'''
    preco_t=0
    for i in lista:
        if i in preco:
        preco_t+=preco[i]
    return round(preco_t,2)