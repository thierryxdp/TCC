def lingua_p(palavra: str) -> str:
    """Retorna essa mesma palavra traduzida para a língua do P.
    Exemplo: Caderno → capadepernopo"""
    
    palavranova = ""
    
    for i in range(0, len(palavra)):
        if (str.lower(palavra[i]) in "aeiou"):
            palavranova += palavra[i] + "p"
        else:
            palavranova += palavra[i]
            
    return palavranova