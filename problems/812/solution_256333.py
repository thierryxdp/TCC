def retira_pontuacao(frase):
   
    s1=str.split(frase,'.')
    s2=str.split(frase,'-')
    s3=str.split(frase,':')
    s4=str.split(frase,';')
    s5=str.split(frase,',')
    s=str.join(' ',(s1)(s2)(s3)(s4)(s5))
    return s