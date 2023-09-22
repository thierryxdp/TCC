def uppCons(frase):
    """Essa função recebe uma frase e retorna caso indentificado 
    uma consoante, a frase com suas consoantes agora em caixa alta.
    Entrada uma frase e saída a sua modificação;
    str->str"""
    indice=0
    upp=""
    while indice<len(frase):
        if frase[indice] not in "AEIOUaeiou" or frase[indice]==" ":
            upp=upp+frase[indice].upper()
        else:
            upp=upp+frase[indice]
        indice+=1
    return upp