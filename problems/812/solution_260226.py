def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    texto=frase
    for pontos in ",:;?!-.":
    retira=texto.replace(pontos, ' ')
    return retira