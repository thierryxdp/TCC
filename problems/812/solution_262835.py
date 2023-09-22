def retira_pontuacao(frase):
    """Função que dada como parâmetro um frase, retorna a frase substituindo todos os sinais de pontuação por espaços.
    Entrada -> str; Saída -> str"""
    
    frase_um = frase
    frase_dois = frase_um.replace ( "..." , " " )
    frase_tres = frase_dois.replace ( "." , " " )
    frase_quatro = frase_tres.replace ( "?" , " " )
    frase_cinco = frase_quatro.replace ( "!" , " " )
    frase_seis = frase_cinco.replace ( "-" , " " )
    frase_sete = frase_seis.replace ( "," , " " )
    frase_oito = frase_sete.replace ( ":" , " " )
    frase_nove = frase_oito.replace ( ";" , " " )
    return frase_nove