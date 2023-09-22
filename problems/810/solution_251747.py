def retira_pontuacao(x1):
    '''/ , : ; . ! ? ...'''
    y1 = str.replace(x,'/',' ')
    y2 = str.replace(y1,',',' ')
    y3 = str.replace(y2,':',' ')
    y4 = str.replace(y3,'.',' ')
    y5 = str.replace(y4,'!',' ')
    y6 = str.replace(y5,'?',' ')
    y7 = str.replace(y6,'...',' ')
    x2 = str.replace(y7,'-',' ')
    n = list.invert(x2)
    return n