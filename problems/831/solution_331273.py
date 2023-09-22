def lingua_p (palavra):
    """dada uma palavra como parametro, retorna a palavra na lingua do p;
    str->str"""
    minuscula=palavra.lower()
    contadora=0
    lingua='p'
    vogal='aeiouáéíóú'
    aux=''
    for i in palavra:
        if palavra[contadora] in vogal:
            aux=aux+palavra[contadora]+lingua+palavra[contadora] 
        if palavra[contadora] not in vogal:
            aux=aux+palavra[contadora]
        contadora+=1
    
    return aux