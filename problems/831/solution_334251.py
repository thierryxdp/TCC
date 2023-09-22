def lingua_p(p):
    """Função que recebe como entrada uma palavra e retorna
essa palavra traduzida para a língua do P, ignorando a di-
ferença entre minúsculas e maiúsculas, traduzindo-a toda em
letras minúsculas.
Assinatura: str -> str
"""
    vogais = ['a','e','i','o','u', 'á', 'é', 'ú']
    l = []
    for x in p:
        if x in vogais:
            l.append(x + "p" + x)
        else:
            l.append(x)
    return str.lower("".join(l))