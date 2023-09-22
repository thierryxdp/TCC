def lingua_p(palavra):
    """função que recebe como parametro uma palavra e retorna a mesma palavra traduzida para lingua do p; str->str"""
    traduz=""
    palavra = str.lower(palavra)
    restricao = "aeiouáâéêíîóôúûãõqwrtypsdfghjklçzxcvbnm"
    for i in range(len(palavra)):
        if palavra[i] not in restricao:
            traduz += palavra[i] + "p" + palavra[i]
        else:
            traduz += palavra[i]
    return traduz