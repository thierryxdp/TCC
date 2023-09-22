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
    frasenova = frasenova.lower ( )
    frasenova = frasenova.split ( ) 
    frasenova = frasenova [ : : - 1 ] 
    frasenova = " ".join ( map ( str , frasenova ) )
    return frasenova