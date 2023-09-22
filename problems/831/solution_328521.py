def linagua_p(palavra):
    """Função que dada uma palavra em português, retorna esta mesma palavra traduzida para a
    língua do P; str -> str"""

    palavraP = ""

    for letra in palavra:
        if letra in "aeiouAEIOUáâãéêíóõôú":
            palavraP += letra + "p" + letra
        if letra not in "aeiouAEIOUáâãéêíóõôú":
            palavraP += letra

    return str.lower(palavraP)