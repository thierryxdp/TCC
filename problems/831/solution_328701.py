def lingua_p(palavra):
    """Dada uma palavra, retorna ela na língua do P;
    string -> string"""
    lista = list(palavra)
    
    for letra in range(0,len(lista)):
        if lista[letra] in "aeiouAEIOU":
            lista[letra]= lista[letra] + "p" + lista[letra]
    
    return str.join("",lista)