def retira_pontuacao(frase):
    '''calcule uma função que, dada uma frase,retorne a frase com todos os caracteres de pontuação substuídos por espaço.str-->str.'''
    frase_nova = (frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    return frase_nova

def inverte(frase2):
    '''calcule uma funcao que, dada uma frase, retorne essa frase na ordem contrária, sem a pontuação e sem letras maiúsculas.str--str.'''
    sem_maiusculas = str.lower(frase2)
    sem_pontuacao = retira_pontuacao(frase2)
    frase2 = str.split(frase2)
    str.join(' ', list.reverse(frase2))