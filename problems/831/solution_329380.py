def lingua_p(plvr):
    """ funcao que recebe uma string "plvr" de entrada e retorna
    essa string traduzida para a língua do P, onde após cada vogal da palavra
    original, é inserido uma letra "p" mais a vogal original """
    """str -> str """
    minusculas = plvr.lower()
    n_plvr = ""
    vogal = "áéíóúaeiouâêôãõ"
    for p in minusculas:
        n_plvr += p
        if p in vogal:
            n_plvr += "p" + p
    return n_plvr
#Casos de testes:
""" lingua_p("Luiz Felipe")
>>> 'lupuipiz fepelipipepe'
    lingua_p("Corações")
>>> 'coporapaçõpõepes'
    lingua_p("COMPUTAÇÃO")
>>> 'copompuputapaçãpãopo' """