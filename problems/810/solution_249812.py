def inverte(x):
    '''
    função que dada uma frase retorna uma outra frase na ondem inversa, sem letras maiusculas
    e sem pontuação
    '''
    y=str.replace(x,'-',' ')
    z=str.replace(y,',',' ') 
    w=str.replace(z,':',' ')
    n=str.replace(w,';',' ')
    k=str.replace(n,'.',' ')
    c=str.replace(k,'?',' ')
    v=str.replace(c,'!',' ')
    frase_minuscula=str.lower(v)
    lista=str.split(frase_minuscula)
    invertido=(reversed(lista))
    lista_pronta=str.join('',invertido)
    
    return lista_pronta