def lingua_p(palavra):
    """ x """
    v = ''
    minusculo = palavra.lower()
    i = 'AEIOUaeiouáéíóúãõâêôû'
    for letras in minusculo:
        v += letras
        if letras in i:
       		  vogais = vogais + 'p' + letras
    return vogais