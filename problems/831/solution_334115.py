def lingua_p(palavra):
    """Função que dada uma palavra, a traduz para a lingua do P. str -> str"""
    palavra = palavra.lower()
    palavra = list(palavra)
    traducao = []
    j = 0
    for p in range(len(palavra)):
        if palavra[p] in "aeiouãéáú":
            traducao.insert(j,palavra[p])
            traducao.insert(j+1,"p")
            traducao.insert(j+2,palavra[p])
            j += 3
        else:
            traducao.insert(j,palavra[p])
            j += 1
    traducao = "".join(traducao)
    return traducao