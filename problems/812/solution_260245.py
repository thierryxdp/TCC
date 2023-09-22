def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    texto=frase
    caractere='-'and'.'and'?'and','and'!'
    for caractere in caractere:
        substituicao=texto.replace(caractere,' ')
        return substituicao