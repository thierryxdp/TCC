def lingua_p(palavra):
    x=str.lower(palavra)
    palavranova=''
    contador=0
    for caractere in palavra:
        if caractere in "aeiou":
            palavranova=palavranova+"p"+caractere
        else:
            palavranova=palavranova+caractere
    return palavranova