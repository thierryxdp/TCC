def linagua_p(palavra):
'''Transforma uma palavra em sua versão da lingua do P;
None -> float'''
    palavra_p = ""
    for c in palavra:
        c = c.lower()
        palavra_p += c
        if c in ["a", "e", "i", "o", "u"]:
            palavra_p += "p" + c
    return palavra_p