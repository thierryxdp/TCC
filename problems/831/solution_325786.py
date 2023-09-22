def lingua_p(string):
    """Função que localiza as vogais presentes na string dada e insere 
    letras "p" após a ocorrência de cada uma."""
    """str-->str"""
    lista_original=list(str.lower(string))
    lista_string=list.copy(lista_original)
    a=0
    for i in lista_original:
        index=list.index(lista_original,i)
        if i in 'aeiou':
            lista_string.insert(index+1,'p')
            lista_string.insert(index+2,lista_string[a])
        a=a+1
    return str.join(lista_string)