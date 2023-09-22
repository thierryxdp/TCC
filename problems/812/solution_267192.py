def retira_pontuacao(frase):
    "função que retira a pontuação da frase dada e substitui por espaços, str --> str"
    a= str.replace(frase,'-',' ')
    b= str.replace(a,',',' ')
    c= str.replace(b,':',' ')
    d= str.replace(c,';',' ')
    e= str.replace(d,'.',' ')
    f= str.replace(e,'!',' ')
    g= str.replace(f,'?',' ')
    frasenova = g
    return frasenova