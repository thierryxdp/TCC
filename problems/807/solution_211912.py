def conta_frases(texto):
    """Dado como entrada um texto contendo frases, ao final de cada uma
    das frases possui um sinal que pode ser um ponto final,
    ponto de exclamação, interrogação, ou reticências,(.,!,?,...),
    retorna o número de frases que este texto possui;
    str->int """
    s0=texto
    s1=str.replace(s0,"!",".")
    s2=str.replace(s1,"?",".")
    s3=str.replace(s2,"...",".")
    return len(str.split(s3,". "))