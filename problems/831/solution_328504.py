def lingua_p(l):
    """Recebe uma palavra e retorna a mesma porém traduzida na lingua do p
    str -> str"""
    a = []
    r = ''
    vogais = "aeiouáéíóúãõâêîôû"
    vogais = vogais+vogais.upper()
    for i in range(len(l)):
        a.append(l[i])
        if l[i] in vogais:
            a.append("p")
            a.append(l[i])
    for i in range(len(a)):
        r = r + a[i]
    return r