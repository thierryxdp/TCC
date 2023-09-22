def substitui(s,x,i):
    '''Essa função retorna a string dada como entrada, mas com 
    a substituição da posição indicada por um outro caractere
    str,str,int->str'''
    string=str(s)
    
    return string[0:i]+ x + string[i+1:]