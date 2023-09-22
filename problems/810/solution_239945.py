def inverte(frase):
    """funcao que,dada uma frase,retorna uma nova frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letr as maiusculas,e sem a pontuacao;str,str->str"""
    lista = (str.split(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'.',' '),'!',' '),'?',' '),',',' '),'-',' ')))
    return  str.lower(str.join(" ",(lista[::-1])))