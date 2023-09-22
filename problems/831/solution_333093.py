def lingua_p(palavra):
    """ Uma função que receba como parâmetro uma palavra
    e em PT e retorne a mesma, traduzida para a língua do P;
    str=>str"""
    v = ''
    minusculo = palavra.lower()
    i = 'AEIOUaeiouáéíóúãõâêôû'
    for letras in minusculo:
        v += letras
        if letras in i:
            vogais += 'p' + letras
    return vogais