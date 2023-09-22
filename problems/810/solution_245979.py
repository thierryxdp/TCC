def inverte(frase):
    """Função que dada uma frase, inverte a ordem de suas palvras, retirando a pontuação e a letra maiúscula."""
    """str->str"""
    for x in ".!?,;:-":
        frase = frase.replace(x, " ")
    frase_nova = str.lower(frase)
    frase_completa = str.split(frase_nova)
    ultima = frase_completa[::-1]
    if len(ultima) == 1:
        return ultima[0]
    if len(ultima) == 2:
        return ultima[0] + " " + ultima[1]
    if len(ultima) == 3:
        return ultima[0] + " " + ultima[1] + " " + ultima[2]
    if len(ultima) == 4:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3]
    if len(ultima) == 5:
        return  ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]
    if len(ultima) == 6:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5]
    if len(ultima) == 7:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5] + " " + ultima[6]
    if len(ultima) == 8:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5] + " " + ultima[6] + " " + ultima[7]
    if len(ultima) == 9:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5] + " " + ultima[6] + " " + ultima[7] + " " + ultima[8]
    if len(ultimo) == 10:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5] + " " + ultima[6] + " " + ultima[7] + " " + ultima[8] + " " + ultima[9]
    if len(ultimo) == 11:
        return ultima[0] + " " + ultima[1] + " " + ultima[2] + " " + ultima[3] + " " + ultima[4]+ " " + ultima[5] + " " + ultima[6] + " " + ultima[7] + " " + ultima[8] + " " + ultima[9] + " " + ultimo[10]