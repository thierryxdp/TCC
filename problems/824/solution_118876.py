def uppCons(frase):
    "funcao que recebe como entrada uma frase e retorna essa frase com todas as consoantes em maiusculas"
i = 0 
while i < len(frase):
    if frase[i] in "abcdefg":
        str.upper(frase[i])
        i = i + 1
        return frase