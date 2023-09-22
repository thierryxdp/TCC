def conta_frases(frase):
    """Função que calcula e retorna o número de frases no texto.
    str-->int"""
   
    frase=str('Preciso tirar um cochilo') +
    str('Meu Deus!') + str('Que horas são') + str('Vou perder minha aula...')
	return len(frase.split())