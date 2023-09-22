def substitui(s,x,i):
    """Retorna a string "s" só que com o caractér da posição "i" trocado
    pelo caractér "x" 
    string , int, int -> string"""
    lista = list(s) 
    lista[i] = str(x)
    nova_string= str.join(",", str(lista))
    nova= nova_string.replace(",",  "")
    nov = nova.replace("'","")
    no = nov.replace(" ", "")
    n= no.strip("[]")
    return no