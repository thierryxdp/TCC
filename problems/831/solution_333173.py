def lingua_p(palavra):
    """recebe uma string e retorna uma nova string, acrescentada após cada vogal a sílaba formada por p e a vogal
    str->str"""
    vogal="aáeéiíoóuú"
    l=""
    for x in palavra:
        if x in vogal:
            l+=(x+"p"+x)
        else:
            l+=x
    return l