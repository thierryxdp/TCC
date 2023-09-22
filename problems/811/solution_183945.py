def colchao(medidas,H,L):
    '''Função que retorna True se o colchao passa por uma porta de altura H e largura L e False se não passa.
    Insira as 3 medidas do colchão em ordem crescente no formato de lista. Insira todos
    os valores em centímetros.
    Entrada: list,int,int. Saída: boleano'''
    if L>=medidas[1] and H>=medidas[0]:
        return True
    elif L>medidas[1] and H>=medidas[2]:
        return True
    elif L>=medidas[0] and H>=medidas[1]:
        return True
    else:
        return False