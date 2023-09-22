def contafrases(frase):
    """Esta funcao recebe uma string e conta o numero de frases nesta string
    entrada: string, saída: int"""
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    frasecomreticencias = (reticencias*3)
    if "..." in frase:
        return (ponto+interrogacao+exclamacao+reticencias-frasecomreticencias)
    else:
        return (ponto+interrogacao+exclamacao)