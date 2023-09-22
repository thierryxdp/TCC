def retira_pontuaçao(frase):
    """ """
    novafrase=''
    for x in range(len(frase)):
        if frase[x] in '?.!,-:;-':
            novafrase+=' '
        else:
            novafrase+=frase[x]
    return novafrase