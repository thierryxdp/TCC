def conta_frases(texto):
    '''jjfjdnnfkggj'''
    if '...' in texto:
        reticicentias_trocadas= str.replace(texto,'...','%')
        frase_reticencias= str.count(reticicentias_trocadas,'%')
        frase_pontofinal=str.count(reticicentias_trocadas,".") 
        frase_exclamacao= str.count(texto,'!')
        frase_interrogacao= str.count(texto,'?')
        return frase_pontofinal+frase_exclamacao+frase_interrogacao+frase_reticencias
    else:
        frase_pontofinal=str.count(texto,".") 
        frase_exclamacao= str.count(texto,'!')
        frase_interrogacao= str.count(texto,'?')
        return frase_pontofinal+frase_exclamacao+frase_interrogacao