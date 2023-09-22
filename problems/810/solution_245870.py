def retira_pontuacao(frase):
    '''calcula uma função que dada uma frase,retorna a frase com todos os caracteres de pontuação substuídos por espaço;
    str-->str.'''
    novafrase = (frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    return novafrase
def inverte(frase2):
    '''calcule uma funcao que, dada uma frase, retorne essa frase na ordem contrária, sem a pontuação e sem letras maiúsculas.str--str.'''
    sem_maiusculas = str.lower(frase2)
    sem_pontuacao = retira_pontuacao(frase2)
    frase2 = str.split(frase2)
    list.reverse(frase2)
    return str.join(frase2)