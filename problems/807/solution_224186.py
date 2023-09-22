def conta_frases(frase):
    """ retorna a quantidade de frases dentro de uma string
		string -> int """
    a = frase.count ('.')
    b = frase.count ('!')
    c = frase.count ('?')
    d = frase.count ('...')
    return a + b + c + d