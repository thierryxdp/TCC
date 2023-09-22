def retira_pontuacao(frase):
    frase1= frase.replase('.','').replase('-','').replase(',','').replase(':','').replase(';','')
    return frase1