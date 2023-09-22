def uppCons(frase):
    """Funcao recebe uma frase qualquer: frase, e retorna a mesma frase com
    todas as suas consoantes maiusculas e com todos os elementos na mesma
    posicao """

    contador = 0
    
    consoantes = ["b", "c", "ç", "d", "f", "g", "h", "j", "k", "l", "m",
                  "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    
    while contador < len(frase):
        if frase[contador] in consoantes:
            maiuscula = frase[contador].upper()
            frase = str.replace(frase, frase[contador], maiuscula)
        contador += 1

    return frase