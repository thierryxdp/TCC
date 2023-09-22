def lingua_p(palavra):
    """Funcao que traduza uma palavra para a lingua do P
    string --> string"""
    traducao = ""
    for i in range(len(palavra)):
        if palavra[i] in "AaáàãEeÉéIiÍíOoÓóõUuÚú":
            traducao = traducao + str.lower(palavra[i])+ "p" + str.lower(palavra[i])
        else:
            traducao = traducao + str.lower(palavra[i])
    return traducao