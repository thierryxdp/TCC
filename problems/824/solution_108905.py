def uppCons(frase):
    '''função que recebe como entrada uma frase e retorna ela com apenas as consoantes em maiúsculo;
    entrada:str
    saida:str'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç': 
            texto=texto+str.upper(frase[i])
            i=i+1
        else:
            texto=texto+str(frase[i])
        	i=i+1
    return texto