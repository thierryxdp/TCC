def inverte(frase):
    """Função recebe um frase que depois a retorna invertida;
    str->str"""
    frase = str.replace(frase, "!",)
    frase = str.replace(frase, "?",)
    frase = str.replace(frase, ".",)
    frase = str.replace(frase, "-",)
    frase = str.replace(frase, ":",)
    frase = str.replace(frase, ";",)
    frase = str.replace(frase, "  ")
    v1 = v1[:: -1]
    v2 = str.join(" ", v1)
    v3 = str.lower(v2)
    return v3