'''Transforma uma palavra em sua versão da lingua do P;
None -> float'''
def linagua_p(palavra):
    palavra_p = ""
    for c in palavra:
        c = c.lower()
        palavra_p += c
        if c in ["a", "e", "i", "o", "u", "á", "à", "ã", "â"]:
            palavra_p += "p" + c
    return palavra_p