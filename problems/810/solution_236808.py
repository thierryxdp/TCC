def inverte(frase):
    sem_pontuacao = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-',' '),',',' '),':',' '),';',' '),'.',' '),'!',' '),'?',' ')
    minusculo = str.lower(sem_pontuacao)
    lista = str.split(minusculo)[::-1]
    junta_lista = str.join(' ',lista)
    return junta_lista