def retira_pontuacao(frase):
    ''' dada uma frase de entrada, substitui todos os caracteres de pontuação por uma string vazia nessa frase str->str '''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'!',' '),'?',' '),'.',' '),'-',' '),',',' '),':',' '),';',' ')
def inverte(frase):
    ''' retorna outra frase que contém as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas e pontuação str->str '''
    return str.join('',str.split(str.lower(retira_pontuacao(frase)),' ')[::-1])