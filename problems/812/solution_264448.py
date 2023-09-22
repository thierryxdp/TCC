def retira_pontuacao (frase):
    '''
    	Recebe uma frase e retorna a frase sem nenhuma pontuação.
        Parâmetro 1: string
        Resultado: string
    '''
    nova_frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase, '...', ' '), '?', ' '), '!', ' '), '.', ' '), '-' , ' '), ',', ' '), ':', ' '), ';', ' ')
    return nova_frase