def lingua_p(plvr):
    """ funcao que recebe uma string "plvr" de entrada e retorna
    essa string traduzida para a língua do P, onde após cada vogal da palavra
    original, é inserido uma letra "p" mais a vogal original """
    minusculas = plvr.lower()
    n_plvr = ""
    vogal = "áéíóúaeiouâêôãõ"
    for p in minusculas:
        n_plvr += p
        if p in vogal:
            n_plvr += "p" + p
    return n_plvr