def inverte(frase):
    frasenova = frase.lower()
    frasenova = frasenova.replace ( "..." , " " )
    frasenova = frasenova.replace ( "." , " " )
    frasenova = frasenova.replace ( "?" , " " )
    frasenova = frasenova.replace ( "!" , " " )
    frasenova = frasenova.replace ( "-" , " " )
    frasenova = frasenova.replace ( "," , " " )
    frasenova = frasenova.replace ( ":" , " " )
    frasenova = frasenova.replace ( ";" , " " ) 
    L = str.split(frasenova, " ")
    list.reverse(L)
    
	
    return str.join(" ", L)