def inverte(x):
    '''
    função que dada uma frase retorna uma outra frase na ondem inversa, sem letras maiusculas
    e sem pontuação.
    str->str
    '''
    y=str.replace(x,'-',' ')
    z=str.replace(y,',',' ') 
    w=str.replace(z,':',' ')
    n=str.replace(w,';',' ')
    k=str.replace(n,'.',' ')
    c=str.replace(k,'?',' ')
    v=str.replace(c,'!',' ')
    final = str.lower(v)
    lista = str.split(final)
    invertida = list(reversed(lista))
    lista_final = ' '.join(invertida)
    
    return lista_final