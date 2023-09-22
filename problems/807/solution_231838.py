def conta_frases(texto):
    """Retorna o número de frases em um texto
    assinatura: str -> int"""
    separador = ['.', '!', '?']
    contador = 0
    for x in range(len(texto)):
  		if texto[x] in separador and texto[x+1] not in separador and  texto[x+2] not in separador and texto[x-1] not in separador and texto[x-2] not in separador: 
      		contador += 1
	return contador