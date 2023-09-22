def lingua_p(string):
    """Função que localiza as vogais presentes na string dada e insere 
    letras "p" após a ocorrência de cada uma."""
    """str-->str"""
    lista_original=list(str.lower(string))
    lista_string=list.copy(lista_original)
    for i in lista_original:
        index=list.index(lista_string,i)
        if i in 'aeiou':
            lista_string.insert(index+1,'p')
            lista_string.insert(index+2,lista_string[index])
    return ''.join(lista_string)