# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
	palavras=str.split(frases," ")
    lista=[]
    for lista_palavras in frases:
    	chave={lista_palavras:1}
        lista=lista + [palavras,]
        return lista