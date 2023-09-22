def lingua_p(palavra):
    """"""
    listap = list(palavra)
    for i in range(len(listap)):
        if "a" or "e" or "i" or"o" or "u" in palavra:
            list.insert(listap,"p",i)
    return listap