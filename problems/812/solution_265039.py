def retira_pontuacao(x):
    'Função que substitui a pontuação de uma frase por espaço.'
    'str->str'
    a=str.replace(x,'.',' ')
    b=str.replace(a,':',' ')
    c=str.replace(b,';',' ')
    d=str.replace(c,',',' ')
    e=str.replace(d,'—',' ')
    return e