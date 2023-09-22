ddef retira_pontuacao(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,',',' '),'/',' '),';',' '),':',' ')
    return str.replace(str.replace(str.replace(str.replace(str.replace(sem_pts1,'.',' '),'-',' '),'!',' '),'?',' '),'...',' ')
def inverte(frase):
     lista1 = str.split(str.lower(retira_pontuacao(frase)))
     list.reverse(lista1)
     return str.join(' ',lista1)
def inverte(frase):
    lista = frase.split()
    lista1 = lista[::-1]
    final = lista1.join()
    return retira_pontuacao(final)