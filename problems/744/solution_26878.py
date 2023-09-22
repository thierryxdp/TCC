def hashtag(palavra):
    """
    Manipula determinada string através de sua inserção do caractere '#"
    em seu meio e em suas extremidades (início e final).
    str -> str

    Parameters:
    palavra: Parâmetro textual, do tipo string (str);

    Returns:
    A string com caractere '#' inserido em seu início, meio e final.
    """
    
    tamanho = len(palavra)
    caracter_central = (tamanho / 2)
    if (caracter_central - 0.5) < int(caracter_central):
        meio_palavra = (round(tamanho / 2))
    else:
        meio_palavra = (round((tamanho / 2)- 0.5))
    tag = ("#" + palavra[0:meio_palavra] + "#" + palavra[meio_palavra:tamanho] + "#")
    return tag