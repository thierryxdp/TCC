def lingua_p(palavra):
    """funcao que recebe uma palavra e retorna a mesma na lingua do p.
    str->str."""
    str_fi=""
    for i in palavra:
        if i in "aeiouAEIOUáéíóú":
            str_fi=str_fi+i+p+i
        else:
            str_fi=i
    return str_fi