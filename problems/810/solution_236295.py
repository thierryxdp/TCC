def inverte(frase):
    '''Funcao que recebe uma frase e retorna
    uma outra frase com as mesmas palavras da
    frase de entrada na ordem inversa, sem 
    letras maiusculas e sem a pontuacao.
    Dados de entrada: str
    Valor de saida: str
    '''
    frase_semPontuacao = retira_pontuacao(frase)
    frase_palavras = str.split(frase_semPontuacao,)
    frase_listaInvertida = frase_palavras[::-1]
    return str.join(" ",frase_listaInvertida)