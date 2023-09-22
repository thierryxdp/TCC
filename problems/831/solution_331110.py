def lingua_p(palavra):
    """Recebe uma palavra em português (string) e retorna
essa mesma palavra traduzida para a língua do P, totalmente
em letras minúsculas.
str -> str
"""
    palavra_p = ""
    for i in palavra:
        if i in "aeiouáéíóúâêîôûãõAEIOUÁÉÍÓÚÂÊÎÔÛÃÕ":
            palavra_p = palavra_p + i + "p" + i
        else:
            palavra_p = palavra_p + i
    return str.lower(palavra_p)