def retira_pontuacao(frase):
    '''Função retorna uma frase substituindo as
    pontuações por espaços'''
    frasenova = frase
    frasenova = frasenova.replace ( "..." , " " )
    frasenova = frasenova.replace ( "." , " " )
    frasenova = frasenova.replace ( "?" , " " )
    frasenova = frasenova.replace ( "!" , " " )
    frasenova = frasenova.replace ( "-" , " " )
    frasenova = frasenova.replace ( "," , " " )
    frasenova = frasenova.replace ( ":" , " " )
    frasenova = frasenova.replace ( ";" , " " )
    return frasenova