def conta_frases(texto):
    """Função que retorna a quantidade de frases dentro do texto onde o seu caractere indica seu final.
    parametros: str->int"""
    N_pont = texto.count(".")
    N_retc = texto.count("...")
    N_Inte = texto.count("?")
    N_Excl = texto.count("!")
    return N_retc + N_pont - (3*N_retc) + N_Excl + N_Inte