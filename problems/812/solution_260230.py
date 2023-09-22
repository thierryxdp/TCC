def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    texto=frase
    for caracteres in ".,:;!?-":
        retira=texto.replace(caracteres, '')
    return retira