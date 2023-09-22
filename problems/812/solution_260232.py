def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    return frase.join([caractere if caractere in ".!?,;:-" else "" for caractere in frase)