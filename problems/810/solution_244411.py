def inverte(frase):
    x1= str.replace(frase,',',' ')
    x2= str.replace(x1,'.',' ')
    x3=str.replace(x2,':',' ')
    x4= str.replace(x3,'-',' ')
    x5=str.replace(x4,';',' ')
    x6=str.replace(x5,'?',' ')
    x7=list(str.replace(x6,'!',' '))
    
    return list.reverse(x7)