def substitui(s,x,i):
    """Retorna a string "s" só que com o caractér da posição "i" trocado
    pelo caractér "x" 
    string , int, int -> string"""
    lista = list(s) 
    lista[i] = str(x)
    nova_string= join(",", str(lista))
    nova_string.replace(", ", "")
    return nova_string