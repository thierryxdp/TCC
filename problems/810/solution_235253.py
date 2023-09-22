def inverte(frase):
    '''funcao que dado uma frase retorna ela invertida
    str->str'''
    x=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,':','#'),';','#'),',','#'),'-','#'),'.','#'),'!','#'),'?','#')
    y=str.replace(x,'#',' ')
    z=str.lower(y)
    
    return z