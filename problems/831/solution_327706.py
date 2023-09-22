def lingua_p():
    "retorna a mesma palavra de entrada transcrita na lingua do p inserindo apos cada vogal a letra p e a sequencia de p mais a vogal"
    vogais = 'ãaáàeéèiíoóuú'
    vogaisup = str.upper(vogais)
    palavra = ''

    for letra in frase:
        if letra in vogais:
            palavra = palavra +  letra + 'p' + letra

        elif letra in vogaisup:
            palavra = palavra +  letra + 'p' + letra

        else:
            palavra = palavra + letra
    return str.lower(palavra)