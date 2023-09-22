def inverte(frase2):
    '''calcule uma funcao que, dada uma frase, retorne essa frase na ordem contrária, sem a pontuação e sem letras maiúsculas.str--str.'''
    inversao = list.reverse(frase2)
    sem_pontuacao = frase2.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    sem_minusculas = str.lower(frase2)
    texto_novo = inversao + sem_pontuacao + sem_minusculas
    return texto_novo