def  retira_pontuacao( frase):
    replac=[',','.',';',':']
    for i in range(replac):
        if i in frase:
            frase.raplace(i,' ')
    return frase