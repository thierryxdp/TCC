def lingua_p(palavra):
    """Retorna a palavra traduzida para a lingua do P.str-->str"""
    traducao=""
    for letra in palavra:
        if letra not in "bcdfghjklmnpqrstvxyz":
            novo=str.lower(letra)+'p'+str.lower(letra)
        if letra in "bcdfghjklmnpqrstvxyz":
            novo=letra
    	traducao=traducao+novo
    return traducao