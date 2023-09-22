def uppCons(frase):
    """Funcao que recebe uma frase e retorna a frase com as consoantes em maiusculo,str->str"""
    i=0
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            str.replace(frase,frase[i],str.upper(frase[i]))
            i=i+1
        return frase