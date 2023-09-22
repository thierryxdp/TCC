def lingua_p (palavra):
    ''' essa funçao recebe uma palavra e a retorna traduzida para a lingua do p
    str.> str'''
    pos=0
    
    for letra in palavra:
        if letra in 'aeiouáéíóúãeiõu':
            list.insert(palavra, pos, 'p')
        pos=pos+1
    return str.join('', palavra)