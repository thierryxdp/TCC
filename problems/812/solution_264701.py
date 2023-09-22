def retira_pontuacao(frase):
    'Substitui toda pontuação por espaço'
    semtrav=str.replace(frase,'-',' ')
    semvirg=str.replace(semtrav,',',' ')
    semdoisp=str.replace(semvirg,':',' ')
    sempvirg=str.replace(semdoisp,';',' ')
    semret=str.replace(sempvirg,'...',' ')
    sempf=str.replace(semret,'.',' ')
    semexc=str.replace(sempf,'!',' ')
    semint=str.replace(semexc,'?',' ')
    return semint