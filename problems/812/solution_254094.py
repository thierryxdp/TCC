def retira_pontuacao(frase)
	'''dada uma frase, retona ela sem os caracteres de pontuacao'''
    lista_final = []
    frase_final = ''
    for i in frase:
        if i not in ',.:;-!?':
            lista_final.append(i)
    for i in lista_final:
        frase_final += i
    return frase_final