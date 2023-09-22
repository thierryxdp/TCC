def lingua_p(palavra):
    """
    string->string"""
    traducao = ""
    vogal = ""
    for i in range(len(palavra)):
        
        if palavra[i] in "aeiouAEIOUáéíóúâêôûîõãüÀÈÌÒÙÁÉÚÍÓàèùìòÂÊÛÎÔÃÕÜ":
            vogal = palavra[i]
            traducao = traducao + vogal + "p" + vogal
        else:
            traducao = traducao + palavra[i]
        
    return  str.lower(traducao)