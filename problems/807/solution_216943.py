def conta_frases(texto):
    """
 Função que dado um texto armazenado em uma string,
 retorna o numéro de frases que aparecem no texto.
 Paramêtro de Entrada: string
 Valor de saida: int
    """
    if "..." in texto:
        p_final= str.count(str.join(" ",str.split(texto,"...")),".")
        p_reticencias= str.count(str.replace(texto,"...","*"),"*")
        p_exclamcao= str.count(texto,"!")
        p_interrogacao= str.count(texto,"?")
        return p_final+p_exclamcao+p_interrogacao+p_reticencias
    else:
        p_final= str.count(texto,".")
        p_exclamcao= str.count(texto,"!")
        p_interrogacao= str.count(texto,"?")
        return p_final+p_exclamcao+p_interrogacao