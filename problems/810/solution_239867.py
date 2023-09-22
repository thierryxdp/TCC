def retira_pontuacao(frase):
    frasel = list(frase)
    for i in range(len(frase)):
        if frasel[i]=='-' or frasel[i]==',' or frasel[i]==':' or frasel[i]==';' or frasel[i]=='!' or frasel[i]=='?' or frasel[i]=='.' or frasel[i]==',':
            frasel[i] = ' '
    
    return ''.join(frasel)

def inverte(frase):
    frase_sp = retira_pontuacao(frase)
    frase_min = frase_sp.lower()
    frase_palavras = frase_min.split()
    frase_invertida = ' '.join(frase_palavras[: :-1])

	return frase_palavras