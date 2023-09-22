def retira_pontuacao(frase):
    for i in range(len(frase)):
        if frase[i]=='-' or frase[i]==',' or frase[i]==':' or frase[i]==';' or frase[i]=='!' or frase[i]=='?' or frase[i]=='.' or frase[i]==',':
            frase[i] = ' '
    return frase