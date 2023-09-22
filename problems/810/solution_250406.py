def retira_pontuacao(frase):
    sem_pts1 = str.replace(str.replace(str.replace(str.replace(frase,',',' '),'/',' '),';',' '),':',' ')
    return str.replace(str.replace(str.replace(str.replace(str.replace(sem_pts1,'.',' '),'-',' '),'!',' '),'?',' '),'...',' ')
def inverte(frase):
     lista1 = str.split(str.lower(retira_pontuacao(frase)))
     list.reverse(lista1)
     return str.join(' ',lista1)