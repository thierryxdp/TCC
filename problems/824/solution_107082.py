def uppCons(frase):
    """funcao que retorna a frase de entrada com todas suas consoantes em maiusculas;
    str -> str"""

    i = 0
    

    while i<=len(frase)-1:

        if frase[i] not in 'AEIOUaeiou':


            frase = frase.replace(frase[i],frase[i].upper())
    

        i+=1


    return frase