def uppCons(frase):
    """Funcao recebe uma frase qualquer: frase e retorna a mesma frase com
    todas as suas consoantes maiusculas, com todos os elementos na mesma
    posicao """

    contador = 0
    
    vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    
    while contador < len(frase):
        if frase[contador] in vogais:
            contador += 1
        else:
            letra = frase[contador]
            maiuscula = letra.upper()
            frase = str.replace(frase, letra, maiuscula)
            contador += 1

    return frase