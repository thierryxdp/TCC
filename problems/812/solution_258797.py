def retira_pontuacao(frase):
    frasel = list(frase)
    for i in range(len(frase)):
        if frasel[i]=='-' or frasel[i]==',' or frasel[i]==':' or frasel[i]==';' or frasel[i]=='!' or frasel[i]=='?' or frasel[i]=='.' or frasel[i]==',':
            frasel[i] = ' '
    
    return ''.join(frasel)