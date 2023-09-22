# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    dicionario = {}
    list_elem = frases.split()
    for i in range(len(list_elem)):
        dicionario[list_elem[i]] = list_elem.count(list_elem[i])     
	return dicionario