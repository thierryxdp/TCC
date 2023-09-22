def lingua_p(palavra):
    '''
   	Traduz uma palavra para a lingua do p.
    
    Entrada/Saida:
    string -> string
    '''
    palavra = palavra.lower()
    p = ''
    for i in palavra:
        p += i
        if i in "aeiouáéíóúã":
            p += 'p' + i
    return p