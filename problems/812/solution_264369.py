def retira_pontuacao(frase):
    """funcao que dada uma frase,retorna a frase onde todos os caracteres de pontuacao sejam substituidos por espaço"""
    a=str.join('',str.split(frase,'.'))
    b=str.join('',str.split(a,','))
    c=str.join('',str.split(b,'?'))
    d=str.join('',str.split(c,'!'))
    e=str.join('',str.split(d,'-'))
       return e