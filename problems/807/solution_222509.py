def conta_frases(frase):
	'''Função retorna a quantidade de frases que 
    um texto possui.String-->Int'''
    quant_ponto=str.count(frase,'.')
    quant_exclamacao=str.count(frase,'!')
    quant_interrogacao=str.count(frase,'?')
    quant_retissencias=srt.count(frase,'...')
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+srt.count(frase,'...')