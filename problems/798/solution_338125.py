# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
	palavras=str.split(frases," ")
    lista=[]
    for lista_palavras in frases:
        lista=lista + palavras
        chave={lista_palavras:1}
        return lista