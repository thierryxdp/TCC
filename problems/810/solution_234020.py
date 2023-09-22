def inverte(string):
    """Retorna uma frase com as palavras de entrada na ordem inversa; string -> string."""
    string = str.replace(string,"!"," ")
    string = str.replace(string,"?"," ")
    string = str.replace(string,"..."," ")
    string = str.replace(string,"."," ")
    string = str.replace(string,","," ")
    string = str.replace(string,"-"," ")
    string = str.replace(string,";"," ")
    str.join(" ",str.split(string[-1::],))