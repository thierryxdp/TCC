def retira_pountuacao(frase):
    new=str.replace(frase,'.',' ')
    naw=str.replace(new,'?',' ')
    now=str.replace(naw,'!',' ')
    nuw=str.replace(now,'-',' ')
    niw=str.replace(nuw,',',' ')
    return niw