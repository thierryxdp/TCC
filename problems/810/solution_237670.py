def inverte(texto):
    """Função que recebe um texto e retorna a mesma de modo invertido
       Parametros: str -> str"""
    texto = texto.lower()
    pontos =['!','?','.',':']
    for testar in pontos:
        if testar != '-' and testar in texto:
            texto = texto.replace(testar,'')
        else:
            texto = texto.replace(testar,' ')
            
    texto = texto.split()
    texto.reverse()
    texto = ' '.join(texto)
    return texto