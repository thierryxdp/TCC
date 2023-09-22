def retira_pontuacao(frase):
    """retorna a frase onde todos os caracteres de pontuação tenham sido substituidos por espaços; str -> str"""
    x=str.replace(frase,'-',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    w=str.replace(z,';',' ')
    a=str.replace(w,'.',' ')
    b=str.replace(a,'!',' ')
    c=str.replace(b,'?',' ')
    d=str.replace(c,'...',' ')
    return d
def inverte(frase):
    """retorna outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa sem letras maiusculas e sem pontuaçao; str -> str"""
    x=retira_pontuacao(frase)
    y=str.lower(x)
    z=str.split(y,' ')
    w=list.reverse(z)
    return w[0]+w[1]+w[2]+w[3]+w[4]+w[5]+w[6]+w[7]+w[8]+w[9]+w[10]+w[11]+w[12]+w[13]+w[14]+w[15]+w[16]+w[17]+w[18]+w[19]+w[20]