def lingua_p(palavra):
    palavra = palavra.lower()
    for letra in palavra:
        if letra in "aeiou":
            eita = letra +'p'+ letra
            lista = palavra.replace(letra, eita)
    return lista