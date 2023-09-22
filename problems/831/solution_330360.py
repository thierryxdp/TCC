def lingua_p (palavra):
    """dada uma palavra como parametro, retorna a palavra na lingua do p;
    str->str"""
    g=palavra.lower()
    y=0
    x='p'
    vogal='aeiouáéíóú'
    aux=''
    while y<len(palavra):
        if palavra[y] in vogal:
            aux=aux+palavra[y]+x+palavra[y] 
        if palavra[y] not in vogal:
            aux=aux+palavra[y]
        y+=1
    
    return aux