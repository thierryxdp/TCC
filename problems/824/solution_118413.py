def uppCons(frase):
    '''Dada uma frase, retorna a frase com todas as suas consoantes em maiúsculas;
    string -> string'''

    i = 0
    nova_frase = ''

    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            nova_frase = nova_frase + frase[i].upper()
        else:
            nova_frase = nova_frase + frase[i]
        i += 1

    return nova_frase