def uppCons(frase):
    'função que recebe uma frase e retorna a mesma frase com todas as consoantes maiúsculas. str->str'
    novafrase:""
    i=0
    while frase[i]<len(frase):
        if frase[i] in "aeiou":
            novafrase+=(lista[i],)
        i+=1
    return novafrase