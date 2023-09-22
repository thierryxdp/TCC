def inverte(frase):
    '''recebe uma frase e retorna uma nova frase sem pontuações, sem letras maiúsculas e de trás para frente.
    str -> str'''
    sem_pontuacao = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'!',' '),'?',' ')
    minusculo = str.lower(sem_pontuacao)
    lista = str.split(minusculo)[::-1]
    junta_lista = str.join(' ',lista)
    return junta_lista