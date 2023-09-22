def lingua_p(palavra):
    """Uma função que receba uma palavra e retoirne a mesma traduzida 
    para o português; str => str"""
	vogais= ''
    minus = palavra.lower()
    valor = 'AEIOUaeiouáéíóúãõâêôû'
    for l in minus:
        vogais += letras
        if letras in valor:
            vogais += 'p' + letras
    return vogais