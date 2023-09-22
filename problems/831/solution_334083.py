def lingua_p(palavra):
    """Esta função recebe uma palavra e a traduz para a lingua do P
    str -> str"""
    palavra = palavra.lower()
    palavra = list(palavra)
    traducao = []
    y = 0
    for x in range(len(palavra)):
        if palavra[x] in "aeiouãéáú":
            traducao.insert(y,palavra[x])
            traducao.insert(y+1,"p")
            traducao.insert(y+2,palavra[x])
            y += 3
        else:
            traducao.insert(y,palavra[x])
            y += 1
    traducao = "".join(traducao)
    return traducao