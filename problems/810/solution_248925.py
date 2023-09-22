def retira_pontuacao (frase):
    '''
    	Recebe uma frase e retorna a frase sem nenhuma pontuação.
        Parâmetro 1: string
        Resultado: string
    '''
    nova_frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '...', ' '), '?', ' '), '!', ' '), '.', ' '), '-' , ' '), ',', ' '), ':', ' '), ';', ' ')
    return nova_frase

def inverte (frase):
    '''
    	Recebe uma frase e inverto a rodem das palavras.
        Parâmetro 1: string
        Resultado: string
    '''
    nova_frase = retira_pontuacao(frase)
    palavras = str.split(nova_frase)
    palavras.reverse()
    return str.lowwer(' '.join(palavras))