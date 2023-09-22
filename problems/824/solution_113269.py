def uppCons(x):
    '''Recebe como entrada uma string e retorna a mesma string com todas as consoantes em maiuscula, str->str'''
    letra=0
    maiuscula=str.upper(x)
    while letra<len(x):
        if x[letra] not in 'ÃÁÀÂAÊÉÈEÍÌÎIOÒÓÔÕÚÙÛUáàãâaeêéèíìîioóòôõúùûu ':
            x=str.replace(x,x[letra],maiuscula[letra])
            letra=letra+1
        else:
            letra=letra+1
    
    return x