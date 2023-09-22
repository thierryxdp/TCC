def uppCons(frase):
    """Função que recebe uma frase e retorna a frase com todas as suas consoantes
    em maiusculas.
    str -> str."""
    contador = 0
    fraseFinal = ''
    while contador < len(frase):
        if frase[contador] not in 'AEIOUaeiou':
            fraseFinal = fraseFinal + str.upper(frase[contador])
        else:
            fraseFinal = fraseFinal + frase[contador]
        contador = contador + 1
    return fraseFinal