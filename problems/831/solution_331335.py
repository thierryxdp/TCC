def lingua_p(palavra):
    """Essa função receberá uma palavra qualquer em português
    e retornará esta mesma palavra traduzida para a língua do
    P. A tradução do português para a língua do P funciona da 
    seguinte forma: após cada vogal da palavra original (em por-
    tuguês), é inserida a sequência de letras 'p' mais a vogal
    original.
    Exemplo: então -> epentapaopo
    
    str -> str
    """
    
    palavra_traduzida = ""
    for letra in palavra:
        if letra in "AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôû":
            letra = str.lower(letra) + "p" + str.lower(letra)
        palavra_traduzida = palavra_traduzida + letra
    return palavra_traduzida