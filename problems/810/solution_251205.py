def inverte(frase):
    '''Função que dada uma frase, retorna outra frase que contem
    as mesmas palavras da frase de entrada, porém na ordem inversa,
    sem letras maiúsculas e sem pontuação
    '''
    
    frase1=retira_pontuacao(frase)
    frase2=frase1.lower()
    frase_lista=frase2.split()
    lista_reversa=frase_lista[::-1]
    frase_reversa=' '.join(lista_reversa)
    return frase_reversa