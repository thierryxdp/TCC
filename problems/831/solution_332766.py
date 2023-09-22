def lingua_p(palavra):
    """Recebe uma palavra e retorna a palavra
    reescrita na língua do p.
    Assinatura: str -> str"""
    np=str.lower(palavra)
    nf=''
    for letra in palavra:
        nf+=letra
        if letra in "aeiouáéíóúâêôã":
            nf+='p'+letra
    return nf