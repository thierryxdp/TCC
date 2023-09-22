def retira_pontuacao(frase):
	"Dada uma frase, a função retorna a frase com todos os caracteres de pontuação substituídos por espaço."
	fraselista=list(frase)
	for caractere in fraselista:
		if caractere in ['.',',','-',':',';','!','?','/','\','(',')']:
			fraselista[fraselista.index(caractere)]=' '
			fraseresultante=''.join(fraselista)
		else:
			continue
	return(fraseresultante)