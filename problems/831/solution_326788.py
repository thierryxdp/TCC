'''Transforma uma palavra em sua versão da lingua do P;
None -> float'''
def lingua_p(palavra):
    palavra_p = ""
    for c in palavra:
        c = c.lower()
        palavra_p += c
        if c in ["a","à","á","ã","â","e","é","ê","i","í","o","ó","ô","õ","u","ú"]:
            palavra_p += "p" + c
    return palavra_p