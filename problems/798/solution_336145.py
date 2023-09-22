# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def freq_palavras(frase):
    lista_frase = frase.split()
    lista_palavras = []
    quantidade_palavras = []
    dicionario = {}
    for i in lista_frase:
        if i not in lista_frase:
            lista_palavras.append(i)
	for i in lista_palavras:
        cont = 0
        for j in lista_frase:
            if j == i:
                cont += 1
 		quantidade_palavras.append(cont)
	for i in range(len(lista_palavras)):
        dicionario(lista_palavras[i]) = quantidade_palavras[i]
	return dicionario