def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    return "".join([caractere if caractere in ".!?,;:-" else "" for caractere in frase)