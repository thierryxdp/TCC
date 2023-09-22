def insere(lista_numero, n):
    '''A função retorna o valor n dado no parâmetro
    na posição correta
    lista -> lista'''
    
    x = [n]
    y = lista_numero
    list.extend(y,x)
    list.sort(y)
    return y