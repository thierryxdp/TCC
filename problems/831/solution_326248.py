def lingua(palavra):
    """Função que dada a entrada uma palavra, retorna a palavra 
    na língua do P.
    str -> str
    """
    palavra = str.lower(palavra)
    vogal = ['a','e','i','o','u','á','â','ã','é','ê','í','ó','õ','ô','ú']
    for indice in vogal:
        if indice in palavra:
            palavra = palavra.replace(indice,indice+'p'+indice)
    return palavra