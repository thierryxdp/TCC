def retira_pontuacao(frase):
        '''Função que substitui todos os caracteres de pontuacao por espaço.
        str-->str'''
        return frase.replace('.',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ')
def inverte(frase):
    lista = retira_pontuacao(frase).split()
    inversa = lista[::-1]
    junta = (' '.join(inversa))
    return junta