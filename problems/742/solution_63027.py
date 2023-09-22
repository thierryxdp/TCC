def substitui(s,x,i):
    """Retorna a string "s" só que com o caractér da posição "i" trocado
    pelo caractér "x" 
    string , int, int -> string"""
    lista = list(s)     #Cria uma lista usando a string inserida
    lista[i] = str(x)   #Substitui o termo i por x
    nova_string= str.join(",", str(lista)) # Cria uma nova string separada por vírgula
    nova_string2= nova_string.replace(",",  "")    # remove as vírgulas
    nova_string3 = nova_string2.replace("'","")             # remove as aspas
    nova_string4 = nova_string3.replace(" ", "")			   # remove os espaços
    nova_string5= nova_string4.strip("[]")					   # remove os colchetes
    return nova_string5