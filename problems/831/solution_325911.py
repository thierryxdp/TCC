def lingua_p(string):
    """Função que localiza as vogais presentes na string dada e insere 
    letras "p" após a ocorrência de cada uma."""
    """str-->str"""
    a=0
    lista_original=list(str.lower(string))
    lista_resultado=[]
    for i in lista_original:
        if i not in 'aeiou':
            lista_resultado=lista_resultado+[i]
        if i in 'aeiou':
            lista_resultado=lista_resultado+[i]
            lista_resultado=lista_resultado+['p']
            lista_resultado=lista_resultado+[i]
    return ''.join(lista_resultado)