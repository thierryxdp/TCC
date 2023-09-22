def uppCons(frase):
    """Funcao calcula e retorna a frase de entrada com todas as suas consoantes em maiusculas;   
    str,str-->str"""
    i=0
    consoante=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiouãéíóú':
            consoante=consoante+str.upper(frase[i])
        else:
            consoante= consoante+frase[i]
        i=i+1
    return consoante