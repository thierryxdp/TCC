def inverte(frase):
    '''funcao que retorna a frase outra frase que tem as mesmas palavras so que na ordem inversa'''
    ponto=frase.count(".")
	exclamacao=frase.count("!")
	interrogacao=frase.count("?")
	reticencias=frase.count("...")
	pontos=ponto+exclamacao+reticencias+interrogacao