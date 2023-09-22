def insere(lista_numero, n):
    '''funcao que dada uma lista ordenada de numeros inteiros e 
    um numero inteiro n, inclua n na posição ordenada correta
    retornando a lista com n incluso em forma crescente'''
    
    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero