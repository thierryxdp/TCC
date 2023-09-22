def retira_pontuacao(frase):
    '''Função que recebe uma frase e retorna essa frase com todos os caracteres de pontuação
    substituídos por espaço;
    str -> str'''
    pontuacao = ['—','-',',',':',';','.','!','?']
    nova_frase = ''
    for i in frase:
        if i not in pontuacao:
            nova_frase += i
        else:
            nova_frase += ' '
            
    return nova_frase