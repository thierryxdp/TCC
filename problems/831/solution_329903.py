def lingua_p(palavra):
    """função que traduz uma palavra para a língua do p
    str->str"""
    palavra2=palavra
    for letra in "AEIOUaeiou":
        palavra2= str.replace(palavra2,letra,letra+"p")
    return palavra2