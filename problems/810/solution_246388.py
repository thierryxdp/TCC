def inverte(frase):
    L = str.split(frase," ")
    list.reverse(L)
    frasenova = frase
    frasenova = str.join(" ", L)
    frasenova = frasenova.replace ( "..." , " " )
    frasenova = frasenova.replace ( "." , " " )
    frasenova = frasenova.replace ( "?" , " " )
    frasenova = frasenova.replace ( "!" , " " )
    frasenova = frasenova.replace ( "-" , " " )
    frasenova = frasenova.replace ( "," , " " )
    frasenova = frasenova.replace ( ":" , " " )
    frasenova = frasenova.replace ( ";" , " " )
    return str.lower(frasenova)