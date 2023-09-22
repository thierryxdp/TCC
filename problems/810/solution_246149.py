def inverte(frase):
    """Função que dada uma frase como parâmetro, retorna um nova frase com as mesmas palavras da frase de entrada em ordem invertida. Entrada -> str; Saída -> str"""    
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
    frasenova = " ".join ( frasenova )
    return frasenova