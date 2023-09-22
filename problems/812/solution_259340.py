def  retira_pontuacao( frase):
    replace=[',','-','.',';',':']
    for i in range(replace):
        if i in frase:
            frase.raplace(i,' ')
    return frase