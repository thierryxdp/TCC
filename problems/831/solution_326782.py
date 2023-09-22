def lingua_p(palavra):
    """Recebe uma palavra(em português) e retorna a mesma palavra para língua do P
       ,ou seja, opós cada vogal da palavra original, é inserida a sequncia de letras
       p mais a vogal original.
       str->str

       Parameters:
       palavra: A palavra que sera tradizida para a lingua do P."""
    palavra2=str.lower(palavra)
    letras=list(palavra2)
    palavraP=""
    for letra in letras:
        if letra not in "qwrtypsdfghjklçzxcvbnm":
            palavraP=palavraP+letra+"p"+letra
        else:
            palavraP=palavraP+letra
    return palavraP