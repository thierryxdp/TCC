# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    #listar com dicionario palavras (Key), frequancia da palavra (value)
    #entrada: frases ; saida: dicionario
	frasen=str.split(frases)
	dicionario={}
	for i in frasen:
		dicionario[i]=list.count(frasen,i)
	return dicionario