def uppCons(string):
    """ Dada uma função que receba uma frase como entrada, vamos retornar a mesma frase
        porem com suas consoantes maisculas.
        Entrada ---> Str
        Saida   ---> Str  """
    j = 0
    x = ''
    while j < len(string):
        if string[j] in 'bcçdfghjklmnpqrstvwxyz':
            x = x + (string[j].upper())
        else:
            x = x + string[j]
        j = j + 1
    return x

""" Teste:
    Resultados Esperados:
    joão gosta de maria ----> João GoSTa De MaRia
    o romano acata amores a damas amadas e Roma ataca o namoro --->
    o RoMaNo aCaTa aMoReS a DaMaS aMaDaS e RoMa aTaCa o NaMoRo
    
    Resultados Obtidos:
    >>> uppCons('joão gosta de maria')
     'João GoSTa De MaRia'
    >>> uppCons('o romano acata amores a damas amadas e Roma ataca o namoro')
     'o RoMaNo aCaTa aMoReS a DaMaS aMaDaS e RoMa aTaCa o NaMoRo'
     
    """