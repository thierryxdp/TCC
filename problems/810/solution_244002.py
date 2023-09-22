def inverte(frase):
    '''calcule uma funcao que, dada uma frase, retorne essa frase na ordem contrária, sem a pontuação e sem letras maiúsculas.str--str.'''
    sem_pontuacao = frase_nova = (frase.replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('.',' ').replace('?',' ').replace('!',' '))
    sem_maiusculas = str.lower(sem_pontuacao)
    inversao = list.reverse(str.split(sem_maiusculas))
    string = str(inversao)
    return string