def retira_vogal(palavra):
    if "a" in palavra:
        return palavra.split("a")
    if "e" in palavra:
        return palavra.split("e")
    if "i" in palavra:
        return palavra.split("i")
    if "o" in palavra:
        return palavra.split("o")
    if "u" in palavra:
        return palavra.split("u")

def lingua_p(palavra):
    l=retira_vogal(palavra)
    p=list
    for x in l:
        p=p+list.insert(l,(x+palavra[x+1]))+"p"+palavra[x+1]
    return p