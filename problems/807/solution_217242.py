def conta_frases(texto:str)->int:
    """Dado um texto em forma de string, retorna a quantidade de frases
    que o texto contém."""
    texto_sem_excl = str.replace(texto,'!',' ')
    texto_sem_inter = str.replace(texto_sem_excl,'?',' ')
    texto_sem_ponto = str.replace(texto_sem_inter,'.',' ')
    
    texto_sem_espaco_triplo = str.replace(texto_sem_ponto,'   ','.')
    texto_sem_espaco_duplo = str.replace(texto_sem_espaco_triplo,'  ','.')
    
    texto_pronto = texto_sem_espaco_duplo[:-1:]
    frases_separadas = str.split(texto_pronto,'.')
    quant_frases = len(frases_separadas)
    return quant_frases