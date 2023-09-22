def retira_pontuacao(frase):
        '''Função que substitui todos os caracteres de pontuacao por espaço.
        str-->str'''
        return frase.replace('.',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ')
def inverte(frase):
    '''Função que,dada uma frase,retorna uma outra frase que contém as mesmas palavras da frase de entrada na ordem inversa,sem letras maiusculas e sem a pontuação.
        str-->str'''
    frase = frase.lower()
    lista = retira_pontuacao(frase).split()
    inversa = lista[::-1]
    junta = (' '.join(inversa))
    return junta