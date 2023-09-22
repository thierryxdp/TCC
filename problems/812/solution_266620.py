def retira_pontuacao(frase):
    s=frase.replace('-',' ')
    s1=s.replace(',',' ')
    s2=s1.replace(':',' ')
    s3=s2.replace(';',' ')
    s4=s3.replace('.',' ')
    total=s4
    return total