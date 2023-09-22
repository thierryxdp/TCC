def retira_pontuacao(frase):

    frase_nova = ''.join(frase).lower()
    frase_nova = re.sub(r'["-,.:@#?!&$]', ' ', frase_nova)
    return(frase_nova)