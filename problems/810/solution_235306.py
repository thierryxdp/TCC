def inverte(lista):
    '''comentario'''
    string1=str.replace(lista,'!','')
    string2= str.replace(string1,'.','')
    string3= str.replace(string2,',','')
    string4= str.replace(string3,'-','')
    string5= str.replace(string4,'?','')
    funcao1= str.lower(string5)
    funcao= str.split(funcao1)
    return funcao