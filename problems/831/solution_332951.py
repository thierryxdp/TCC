def lingua_p(palavra):
    '''função em que dada uma palavra (em portugues) e retorne esta mesma palavra
    traduzida para a lingua do P; str -> str'''
    vogais= ''
    m= palavra.lower()
    v= 'aeiouAEIOU'
    for letra in m:
         vogais= vogais + letra
        if letra in v:
            vogais = vogais + 'letra' + letra 
    return vogais