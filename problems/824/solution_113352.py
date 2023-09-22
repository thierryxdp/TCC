def uppCons(frase): 
    '''funçao que retorna a frase de entrada substituindo as consoantes por maiúscula'''
    '''str->str'''
    i=0
    upcons=''
    while i < len(frase): 
        if frase[i] in "bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ": 
            upcons=upcons+ str.upper(frase[i]) 
        else:
            if frase[i] in "!?,.- aãáâeéêíióôoõuúAÃÁÂÉÊEIÍOÔÕÓUÚ": 
                upcons=upcons+(frase[i])
        i=i+1
    return upcons