def conta_frases(texto):
    """Função que dado um texto armazenado em uma string, conta o número 
       de frases que aparecem nesse texto.
       
       Parameters:
       texto: Texto escolhido para a contagem de frases
       
       Returns: 
       Retorna o número de frases do texto
       str -> int"""
    t = texto
    return len(str.split(t,'.')) + len(str.split(t,'!')) + len(str.split(t,'?')) - len(str.split(t,'...'))