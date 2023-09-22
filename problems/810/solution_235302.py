def inverte(lista):
    '''comentario'''
    string1=str.replace(lista,'!','')
    string2= str.replace(string1,'.','')
    string3= str.replace(string2,',','')
    string4= str.replace(string3,'-','')
    string5= str.replace(string4,'?','')
    funcao= str.split(lista)
    termos=len(funcao)
    return string5