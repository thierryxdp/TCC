def inverte(frase):
    '''função que recebe uma frase e retorna a frase invertida 
    sem as letras maiúsculas e sem as pontuações'''
    frasenova = frasenova.replace ( "..." , " " )
    frasenova = frasenova.replace ( "." , " " )
    frasenova = frasenova.replace ( "?" , " " )
    frasenova = frasenova.replace ( "!" , " " )
    frasenova = frasenova.replace ( "-" , " " )
    frasenova = frasenova.replace ( "," , " " )
    frasenova = frasenova.replace ( ":" , " " )
    frasenova = frasenova.replace ( ";" , " " )
    frasenova = frasenova.lower()
    frasenova = frasenova.split()
    frasenova = frase [::-1]
    frasenova = frasenova.reverse ("frasenova")
    return frase