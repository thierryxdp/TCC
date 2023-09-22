# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    '''funcao que retorna um dicionario onde cada palavras
    da frase e sitada as vezes que ela se repete'''
    a = str.split(frase)
    dicio = {}
    for palavra in a:
        if palavra not in dicio:
            dicio[palavra]=1
		else:
            dicio[palavra]+=1
	return dicio