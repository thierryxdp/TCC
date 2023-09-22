def CARALHO(texto):
    """
 Função que dado um texto armazenado em uma string,
 retorna o numéro de frases que aparecem no texto.
 Paramêtro de Entrada: string
 Valor de saida: int
    """
    p_final=str.count(texto,".")
    p_exclamcao=str.count(texto,"!")
    p_interrocagacao=str.count(texto,"?")
    
    return p_final+p_exclamcao+p_interrogacao