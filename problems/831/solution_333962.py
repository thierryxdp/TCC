def lingua_p(palavra):
    """Esta função recebe uma palavra e a traduz para a lingua P
    str -> str"""
    palavra = palavra.lower()
    palavra = list(palavra)
    traducao = []
    j = 0
    for i in range(len(palavra)):
        if palavra[i] in "aeiouÃ£Ã©Ã¡Ãº":
            traducao.insert(j,palavra[i])
            traducao.insert(j+1,"p")
            traducao.insert(j+2,palavra[i])
            j+= 3
        else:
            traducao.insert(j,palavra[i])
            j+= 1
    traducao = "".join(traducao)
    return traducao