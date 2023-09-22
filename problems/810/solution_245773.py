def retira_pontuacao(texto):
    #pontuação='-',',',':',';','.','!','?','...'
    frase=str.replace(texto,'-',' ')
    frase2 = str.replace(frase, ',', '')
    frase3 = str.replace(frase2, ':', '')
    frase4 = str.replace(frase3, ';', '')
    frase5 = str.replace(frase4, '.', '')
    frase6 = str.replace(frase5, '!', '')
    frase7 = str.replace(frase6, '?', '')
    frase8 = str.replace(frase7, '...', '')
    return frase8

def inverte(texto):
    sem_pontuacao = retira_pontuacao(texto)
    frase=str.lower(sem_pontuacao)
    lista=str.split(frase,' ')
    list.reverse(lista)
    invertido=str.join(' ',lista)
    return invertido.strip()