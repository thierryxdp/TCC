def conta_frase
"""Essa função conta quantas frases tem no texto informado como entrada. Os
parâmtetros que definem o que é uma frase são o ponto final, reticências e ponto
de excalmação. str,int"""
    string = str1.count(".")
    string2 = str1.count("...")
    string3 = str1.count("!")
    return string+string2+string3