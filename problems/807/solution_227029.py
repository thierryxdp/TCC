def conta_frases(a):
	'''Essa função conta o número de frases que aparece no texto'''
	retirar1= a.split('.')
    retirar2= a.split('!')
    retirar3= a.split('?')
    retirar4= a.split('...')
    contagem= (len(retirar1)+len(retirar2)+len(retirar3)+len(retirar4)
    return contagem