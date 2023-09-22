def lingua_p(palavra):
    """ A funçao lingua_p recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P. Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original. 
        
        Parameters:
            palavra = palavra a ser traduzida para a lingua do p

        Testes:
            lingua_p("banana") = "bpanpanpa"
            lingua_p("comida") = "cpompidpa"
            lingua_p("aulas") = "papulpas"
            
        Returns:
            palavra inserida traduzida para a língua do P e toda em minuscula.
            str --> str
    """
    str.lower(palavra)
    resultado = ""
    for x in palavra:
        if x in "aeiou":
            resultado = resultado + "p" + x
        else: 
            resultado = resultado + x
    return resultado