def lingua_p(palavra):
    """Uma função que receba uma palavra e retorne a mesma traduzida 
    para o português; str => str"""
	v = ''
    minusculo = palavra.lower()
    x = 'AEIOUaeiouáéíóúãõâêôû'
    for letras in minusculo:
        v += letras
        if letras in x:
            vogais += 'p' + letras
    return vogais