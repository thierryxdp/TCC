def retira_pontuacao(frase):
	"Dada uma frase, a função retorna a frase com todos os caracteres de pontuação substituídos por espaço."
	fraselista=list(frase)
        def substituidor(caractere):
            if caractere in ['.',',','-',':',';','!','?','(',')']:
                caractere=' '
            return(caractere)
    listaresult=list(map(substituidor,fraselista))
    return(''.join(listaresult))