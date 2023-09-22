def altera_frase(frase,palavra,posicao=0):
    """Função separa as palavras da frase em uma lista pelo espaço entre elas,
    verifica se alguma palavra é a palavra recebida pela função. Caso esteja na lista,
    retorna a função com a primeira vez em que ela aparece trocada por uma versão
    sua inteiramente maiúscula. Caso não esteja na lista, insere na posição dada
    a palavra e junta os elementos da lista com um um espaço entre os elementos/palavras.
    str, str, int-> str"""
	frase_nova=frase.split()
	if palavra in frase_nova:
		return frase.replace(palavra,palavra.upper(),1)
	else:
		frase_nova.insert(posicao,palavra)
		frase_nova=str.join(" ",tuple(frase_nova))
		return frase_nova