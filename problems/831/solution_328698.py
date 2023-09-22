lingua_p(palavra):
    """Dada uma palavra, retorna ela na língua do P;
    string -> string"""
    lista = list(palavra)
    
    for letra in lista:
        if letra in "aeiou":
            lista[letra]= "p" + lista[letra]
    
    return str.join("",lista)