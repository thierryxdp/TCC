def inverte(lista):
    '''funcao que retorna a mesma frase, porem de forma inversa 
    e sem os caracteres de pontuacao e com todas as letras minusculas 
    str->str'''
    string1=str.replace(lista,'!','')
    string2= str.replace(string1,'.',' ')
    string3= str.replace(string2,',',' ')
    string4= str.replace(string3,'-',' ')
    string5= str.replace(string4,'?',' ')
    
    funcao1= str.lower(string5)
    funcao2= str.split(funcao1)
    
    lista1= funcao2[::-1]
    lista2= str.join(' ',lista1)
    
    return lista2