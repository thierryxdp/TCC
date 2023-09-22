def retira_pontuacao(frase):
	pontuacao = str(' ')
	frase = str.replace(frase,'.',pontuacao)
	frase = str.replace(frase,',',pontuacao)
	frase = str.replace(frase,';',pontuacao)
	frase = str.replace(frase,':',pontuacao)
	frase = str.replace(frase,'_',pontuacao)
	frase = str.replace(frase,'-',pontuacao)
	frase = str.replace(frase,'!',pontuacao)
	frase = str.replace(frase,'?',pontuacao)
	return frase

def minusculo(frase):
    frases = str.lower(retira_pontuacao(frase))
    return frases

def inverte(frase):
    """Função que dada uma frase, retorna outra que contenha as mesmas palavras da frase de entrada, mas na ordem inveresa"""
    sequencia = str.split(minusculo(frase))
    list.reverse(sequencia)
    return str.join(' ',sequencia)