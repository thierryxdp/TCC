def inverte(frase):
    '''funcao que dado uma frase retorna a mesma invertida
    str->str'''
    x=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,':','#'),';','#'),',','#'),'-','#'),'.','#'),'!','#'),'?','#')
    y=str.replace(x,'#',' ')
    z=str.lower(y)
    w=str.split(z,' ')
    for t in reversed(w):   
        r=str.join(t,' ')
        return r