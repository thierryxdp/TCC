def lingua_p(palavra):

    traducao = ""

    for i in palavra:
        if i in "aeiouAEIOU":
            i = i + "p" + i
        traducao = traducao + i

    return traducao.lower()