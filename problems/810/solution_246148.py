def inverte(frase):
    """dada uma frase, a função retorna a frase com suas palavras na
    ordem inversa, em letra minúscula e sem pontuação.
    str -> str"""
    
    frase1 = frase
    frase2 = frase1.replace ( "..." , " " )
    frase3 = frase2.replace ( "." , " " )
    frase4 = frase3.replace ( "?" , " " )
    frase5 = frase4.replace ( "!" , " " )
    frase6 = frase5.replace ( "-" , " " )
    frase7 = frase6.replace ( "," , " " )
    frase8 = frase7.replace ( ":" , " " )
    frase9 = frase8.replace ( ";" , " " )
    
    frasenova = frase9.lower()
    fraseseparada = frasenova.split()
    inversao = fraseseparada[::-1]
    frasefinal = str.join(" ",inversao)
    
    return frasefinal