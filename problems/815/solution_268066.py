def insere(lista_numero, n):
    '''
        Função que retorna uma lista ordenada de números inteiros e um número inteiro n.
        lista(string) => lista
    '''
    tamanho = len(lista_numero)
    
    if(n >= lista_numero[tamanho-1]):
        lista_numero.insert(tamanho, n)
    else:
        for i in range(0, len(lista_numero)):
            if(n <= lista_numero[i]):
                lista_numero.insert(i, n)
                break
    return lista_numero