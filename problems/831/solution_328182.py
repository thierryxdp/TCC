def lingua_p(frase):
    """função recebe uma frase normal e a traduz a língua do p, ou seja adiciona as palavras uma sílaba a mais quando encontra uma vogal incluindo a letra p e a vogal anterior a nova sílaba. str->str."""
    frasep=[]
    for l in frase:
        if l in "aeiouAEIOUáéíóú":
            frasep.append(l.lower()+"p"+l.lower())
        else:
            frasep.append(l.lower())
    return "".join(frasep)