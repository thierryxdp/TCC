def retira_pontuacao(frase):
     "Substitui todas as pontuações de uma frase por espaço "
        frase=frase.replace('...',' ')
        frase=frase.replace('.',' ')
        frase=frase.replace('!',' ')
        frase=frase.replace('?',' ')
     	frase=frase.replace('-',' ')
     	frase=frase.replace(',',' ')
     	frase=frase.replace(';',' ')
     	frase=frase.replace(':',' ')
     	return frase