def lingua_p(palavra):

# retorna uma palavra em portugues traduzida para lingua do P, dado uma string "palavra"
    
    traducao = ""

    for i in palavra:
        if i in "aeiouáéíóúãõAEIOU":
            i = i + "p" + i
        traducao = traducao + i

    return traducao.lower()