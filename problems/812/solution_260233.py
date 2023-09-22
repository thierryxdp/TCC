def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    texto=frase
    for caractere in '[.,;:?!-]':
        substituicao=texto.replace(caractere,'')
        return substituicao