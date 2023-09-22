def substitui(s, x, i):
    """
    Em uma string 's', substitui a ("i"nésima)° letra por 'x', que pode ser um número.

    Em caso de i > numero de elementos na string, retornará erro.
    Em caso de x conter zero como primeiro número, sem ser um float, retornará erro.
    Em caso de i < 0, O valor séra diferente do esperado.

    str, str/float, int -> str
    """

    sN = s[0 : i] + str(x) + s[i+1 : len(s)]

    return sN

    #Casos testes: substitui('Fala pessoal', '-', 5) -> 'Fala-pessoal'
    #Casos testes: substitui('A culpa disso ter acontecido é do x', 0.6, 35) -> 'A culpa disso ter acontecido é do 0.6'
    #Casos testes: substitui('Quero jogar', 'l', 7) -> 'Quero logar'