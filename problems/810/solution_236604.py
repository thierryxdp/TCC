def inverte(frase):
    '''Função que inverte a ordem das palavras na frase inserida como argumento.
    Também remove as possíveis pontuações da frase. Entrada: str. Saída: str.'''
    frase= retira_pontuacao(frase)
    frase=str.lower(frase)
    lista=str.split(frase)
    return str.join(' ',lista[::-1])