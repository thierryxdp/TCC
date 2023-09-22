def retira_pontuacao(frase):
    """Dada uma string, a função retorna a frase substituindo todos os
    caracteres de pontuação por espaços.
    str ->str"""
    
    frase1 = frase
    frase2 = frase1.replace ( "..." , " " )
    frase3 = frase2.replace ( "." , " " )
    frase4 = frase3.replace ( "?" , " " )
    frase5 = frase4.replace ( "!" , " " )
    frase6 = frase5.replace ( "-" , " " )
    frase7 = frase6.replace ( "," , " " )
    frase8 = frase7.replace ( ":" , " " )
    frase9 = frase8.replace ( ";" , " " )
    return frase9