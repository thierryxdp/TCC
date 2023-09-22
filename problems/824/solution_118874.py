def uppCons(frase):
    "funcao que recebe como entrada uma frase e retorna essa frase com todas as consoantes em maiusculas"
    return join(caractere.upper()
                if caractere in "abcdefgh"
                else caractere 
                for caractere in frase