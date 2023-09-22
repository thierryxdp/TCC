def posLetra(string, letra, n):
    """dada uma string, uma letra e um número n, a função retorna em que posição da string a letra se encontra pela 
    n-ésima vez. Caso menos ocorrências da letra na string existam do que o n pedido, a função retorna -1; str, str, int
    -> int"""
    numero_ocorrencias = str.count(string, letra)
    
    if numero_ocorrencias < n:
        return -1
    
    i = 0
    ocorrencias = []
    
    while i < len(string):
        if string[i] == letra:
            ocorrencias = ocorrencias + [i]
        i = i + 1
        
    return ocorrencias[n-1]