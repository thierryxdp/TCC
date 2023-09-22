def lingua_p(palavra):
    '''função em que dada uma palavra (em português) retorne a mesma palavra
    traduzida para a língua do P e toda em minúsculo;
    str -> str'''
    p1=palavra.lower()
    p2=''
    for l in p1:
        if l in 'aeiouáéíóúãõàèìòùâîêôû':
            p2+=l+'p'+l
        else: #quando for consoante
            p2+=l
    return p2