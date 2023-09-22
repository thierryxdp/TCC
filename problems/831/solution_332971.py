def lingua_p(palavra):
    '''função em que dada uma palavra (em portugues) e retorne esta mesma palavra
    traduzida para a lingua do P; str -> str'''
    vogais= ''
    m= palavra.lower()
    v= 'AEIOUaeiouáéíóúãõâêôû'
    for letras in m:
        vogais+= letras
        if letras in v:
            vogais += 'p' + letras
    return vogais