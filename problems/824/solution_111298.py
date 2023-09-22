def uppCons(frase: str)-> str:
    """Dada uma frase, a função retorna a frase com todas as suas consoantes
    em maiúsulas"""
    novafrase = list()
    i = 0
    while (i < len(frase)):
        if (str.lower(frase[i]) in "qwrtypsdfghjklçzxcvbnm"):
            list.append(novafrase, str.upper(frase[i]))
        else:
            list.append(novafrase, frase[i])
        i += 1
    return str.join("", novafrase)