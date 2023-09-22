def retira_pontuacao(x):
    """"Função que dado um parametro retorna o mesmo sem pontuação
    string -> string"""
    x1 = str.replace(x,'-',' ')
    x2 = str.replace(x1,':',' ')
    x3 = str.replace(x2,';',' ')
    x4 = str.replace(x3,'!',' ')
    x5 = str.replace(x4,'?',' ')
    x6 = str.replace(x5,',',' ')
    x7 = str.replace(x5,'.',' ')
    return x7