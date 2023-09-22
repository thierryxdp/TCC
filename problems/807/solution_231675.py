def conta_frases(texto):
    
   	"""Funçao que recebe como parametro um texto
    e retorna quantas frases nele possui."""
    
    qtd_pont = 0
    i = 0
    while i < len(texto):
        if texto[i] in '.','!','?','...':
            qnt_pont = qtd_pont + 1
        i = i + 1
    return qtd_pont