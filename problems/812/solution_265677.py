def retira_pontuacao(frase):
    """Recebe uma frase x e substitui todos os elementos de pontuação por ' '.
    Retorna uma frase sem pontuação alguma.
    Assinatura str -> str"""
    novafrase=''
    for x in range(len(frase)):
        if frase[x] in "?.!,—:;-":
            novafrase+=' '
        else:
            novafrase+=frase[x]
    
    return novafrase