def lingua_p(palavra):
    """funcao wue recebe uma palavra e retorna a mesma na lingua do p.
    str->str."""
    strfi=""
    for i in palavra:
        if i in "aeiouAEIOUáéíóú":
            strfi=strfi+i+"p"+i
        else:
            strfi=strfi + i
    return strfi