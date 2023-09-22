def lingua_p(palavra):
    """Uma função que receba uma palavra e retorne a mesma traduzida 
    para o português; str => str"""
	v = ''
    m = palavra.lower()
    x = 'AEIOUaeiouáéíóúãõâêôû'
    for l in m:
        v += l
        if l in x:
        	v += 'p' + l
    return v