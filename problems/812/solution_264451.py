def retira_pontuacao(frase):
	"""""""
    semexc=str.replace(frase, '!', ' ')
    seminterr=str.replace(semexc, '?', ' ')
    semreti=str.replace(seminterr, '...', ' ')
    semponto=str.replace(semreti, '.', ' ')
    semvirg=str.replace(semponto, ',', ' ')
    sempontovirg=str.replace(semvirg, ';', ' ')
    semtrav=str.replace(sempontovirg, '-', ' ')
    semdoispontos=str.replace(semtrav, ':', ' ')
    return semdoispontos