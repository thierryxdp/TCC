def retira_pontuacao(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,',',' '),'/',' '),';',' '),':',' ')
    return str.replace(str.replace(str.replace(str.replace(str.replace(sem_pts1,'.',' '),'-',' '),'!',' '),'?',' '),'...',' ')
def inverte(frase):
    lista = frase.split()
    lista1 = lista[::-1]
    final = lista1.join()
    return retira_pontuacao(final)