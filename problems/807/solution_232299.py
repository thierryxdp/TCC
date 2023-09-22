def conta_frases(texto):
    """Função que mostra a quantidade de frases em um texto utilizando como demarcação as pontuações; str-> int"""
    x=str.count(texto,'.')
    y=str.count(texto,'!')
    z=str.count(texto,'?')
    resultado=x+y+z
    return resultado