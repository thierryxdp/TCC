def lingua_p (palavra):
    ''' essa funçao recebe uma palavra e a retorna traduzida para a lingua do p
    str.> str'''
    str.lower(palavra)=p1
    lista=list(p1)
    pos=0
    
    for letra in lista:
        if letra in 'aeiouáéíóúãeiõu':
            list.insert(lista, pos, 'p') + letra
        pos=pos+1
    return str.join('', lista)