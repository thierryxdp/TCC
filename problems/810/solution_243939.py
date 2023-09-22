def retira_pontuacao(frase):
    '''calcule uma função que, dada uma frase,retorne a frase com todos os caracteres de pontuação substuídos por espaço.str-->str.'''
    return frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
def inverte(frase2):
    inversao = list.reverse(frase2)
    sem_pontuacao = retira_pontuacao(frase2)
    sem_minusculas = str.lower(frase2)
    texto_novo = inversao + sem_pontuacao + sem_minusculas
    return texto_novo