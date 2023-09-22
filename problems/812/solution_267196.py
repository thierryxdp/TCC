def retira_pontuacao(frase):
    r1=str.replace(frase,"?","")
    r2=str.replace(r1,",","")
    r3=str.replace(r2,":","")
    r4=str.replace(r3,";","")
    r5=str.replace(r4,".","")
    r6=str.replace(r5,"!","")
    return r6