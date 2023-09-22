def inverte(x):
    '''/ , : ; . ! ? ...'''
    y1 = str.replace(x,'/',' ')
    y2 = str.replace(y1,',',' ')
    y3 = str.replace(y2,':',' ')
    y4 = str.replace(y3,'.',' ')
    y5 = str.replace(y4,'!',' ')
    y6 = str.replace(y5,'?',' ')
    y7 = str.replace(y6,'...',' ')
    y8 = str.replace(y7,'-',' ')
    y9 = str.replace(y8,'  ',' ')
    
    z1 = y9.split()
    z2 = z1[::-1]
    z3 = ' '.join(z2)
    return z3