def concatenacao(a, b):
    """Dados 'a' e 'b' como entrada, a função retorna a concatenação das duas strings.
       str, str -> concatenação da str
       Explicação: A concatenação é designada através do operador '+' e é resulta na 
       união de dois termos. Nesse caso, a união será de duas strings 'a' e 'b',
       no formato 'abba'"""
    x = a+b
    y = b+a
    return x+y
#Teste 1:
#concatenacao('a', 'b')--> 'abba'

#Teste 2:
#concatenacao('Lai','za')--> 'LaizazaLai'

#Teste 3:
#concatenacao('Py','thon')--> 'PythonthonPY'