def conta_frases(texto):
    texto1=(str.split(texto, '...'))
    n1=(len(texto1)-1)
   	texto2=(str.split(texto1[0], '?'))
    n2=len(texto2)-1
    texto3=(str.split(texto1[0], '!'))
    n3=len(texto3)-1
    texto4=(str.split(texto1[0], '.'))
    n4=len(texto4)-1
    
    
    return n1