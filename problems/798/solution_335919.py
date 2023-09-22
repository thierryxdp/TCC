#def freq_palavras(frases):
    listaFrases=frases.split(" ")
    dicionarioF={}
    for i in range(len(listaFrases)):
        dicionarioF[listaFrases[i]]=listaFrases.count(listaFrases[i])
	return dicionarioF Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis