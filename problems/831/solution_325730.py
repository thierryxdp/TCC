def lingua_p(frase):
    """Essa funcao recebe uma frase e retorna ela
       traduzida para a lingua do P, onde, sempre apos
       uma vogal eh adicionado o P mais a vogal anterior a ele.
       str, - str"""
    frase = frase.lower()
    frase_nova = ""
    for i in frase:
        if i in "aeiou":
            frase_nova += i+"p"+i
        else:
            frase_nova += i
    return frase_nova