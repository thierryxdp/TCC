def uppCons (frase):
    """funcao que recebe uma frase e retorna somente as consoantes dessa frase em maisculo;
       str->str"""
    consoantes=''
    i=0
    while i<(len(frase)):
        if frase[i] not in "AEIOUaeiou":
           frase=frase.replace(frase[i], frase[i].upper() )
        i=i+1   
    return frase