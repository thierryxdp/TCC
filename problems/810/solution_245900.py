def inverte(frase):
    '''função que recebe uma frase e retorna a frase invertida 
    sem as letras maiúsculas e sem as pontuações'''
    frasenova = frase
    frasenova = frasenova.replace ( "..." , " " )
    frasenova = frasenova.replace ( "." , " " )
    frasenova = frasenova.replace ( "?" , " " )
    frasenova = frasenova.replace ( "!" , " " )
    frasenova = frasenova.replace ( "-" , " " )
    frasenova = frasenova.replace ( "," , " " )
    frasenova = frasenova.replace ( ":" , " " )
    frasenova = frasenova.replace ( ";" , " " )
    frasenova = frasenova.reverse ('frasenova')
    return frasenova