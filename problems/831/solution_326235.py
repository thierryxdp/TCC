#6 ?
def lingua_p(palavra):
    palavra=str.lower(palavra)
    string=''
    for caracter in palavra:
        if caracter in 'aeiouáéíóúãõâêîôû': #qnd aparece uma vogal, insiro p+vogal
            string=string+caracter+'p'+caracter
        else:
            string=string+caracter
    return string