def conta_frases(a):
    """utilizando uma funcao python para contar o numero de ocorrencias de
    um determinado valor em uma string, verificamos atraves da pontuacao quantas
    frases existem neste texto. Para nao obter conflito de valores entre
    '.' e '...' retiramos o dobro do valor de '...' encontrados
    string -> int"""
    return (a.count(".")+a.count("?")+a.count("!"))- 2*a.count("...")