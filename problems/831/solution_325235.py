def lingua_p(palavra):
    '''Retorna a palavra dada traduzida para a língua do p;
    str -> str'''
    palavra=str.lower(palavra)
    palavra_p=''
    for i in palavra:
        if i in 'abcde':
            palavra_p=palavra_p+i+'p'+i
    return palavra_p