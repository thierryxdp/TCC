def lingua_p(palavra):
    """
    string->string"""
    traducao = ""
    vogal = ""
    for i in range(palavra):
        
        if palavra[i] in "aeiouAEIOU":
            vogal = palavra[i]
            traducao = traducao + vogal + "p" + vogal
        else:
            traducao = traducao + palavra[i]
        
    return traducao