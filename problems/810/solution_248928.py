def retira_pontuacao(frase):
	"""Esta funcao recebe uma frase e substitui todas as pontuacoes por
    espacos.
    Entrada: str
    Saida: str""""
    semexc=str.replace(frase, '!', ' ')
    seminterr=str.replace(semexc, '?', ' ')
    semreti=str.replace(seminterr, '...', ' ')
    semponto=str.replace(semreti, '.', ' ')
    semvirg=str.replace(semponto, ',', ' ')
    sempontovirg=str.replace(semvirg, ';', ' ')
    semtrav=str.replace(sempontovirg, '-', ' ')
    semdoispontos=str.replace(semtrav, ':', ' ')
    removeduploesp=str.replace(semdoispontos, '  ', ' ')
    return semdoispontos

def inverte(frase):
    """"""
    return retira_pontuacao(frase)