def uppCons(frase):
    """funcao que recebe uma frase e retorna a frase com todas as suas consoantes em maiusculas;
    string->string"""
    i=0
    novafrase=''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÃãÁáÂâ