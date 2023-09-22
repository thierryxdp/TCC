def concatenacao(a, b):
    """
    Concatena as variáveis a e b, de maneira 'abba'
    Incluir a e b entre as aspas ('') caso não seja valor numérico
    str/float, str/float -> str
    """
    p = str(a) + str(b) + str(b) + str(a)

    return p

    #Casos testes: concatenacao('a', 'b') -> 'abba'
    #Casos testes: concatenacao('te', 's') -> 'tesste'
    #Casos testes: concatenacao('oi', 67) -> 'oi6767oi'