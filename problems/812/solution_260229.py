def retira_pontuacao(frase):
    '''funçao que recebe uma frase e troca as pontuaçoes por espaço'''
    texto=frase
    import re
    retira=re.sub(r'[.,:;!?-]', texto, '')
    return retira