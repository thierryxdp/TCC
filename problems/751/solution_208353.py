def quant_palavras(frase):
  
    '''str -> int'''
    
    x = str.split(frase,' ')

    if x[0]!='' and x[-1]!='':
        return len(x)

    if x[0]=='' and x[-1]!='':
        return len(x)-1

    if x[0]!='' and x[-1]=='':
        return len(x)-1

    if x[0]=='' and x[-1]=='':
        return len(x)-2