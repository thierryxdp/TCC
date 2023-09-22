def conta_frases(texto: str) -> int:
    num_pfinal = str.count(texto, ".")
    num_pexcl = str.count(texto, "!")
    num_pinterrog = str.count(texto, "?")
    num_retic = str.count(texto, "...")
    
    return num_pfinal + num_pexcl + num_pinterrog + num_retic