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
    return removeduploesp

def inverte(frase):
    """"""
    semponto=retira_pontuacao(frase)
    return semponto