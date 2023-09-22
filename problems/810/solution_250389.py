def retira_pontuacao(string):
    """
    Essa função apos receber uma string qualquer como argumento
    ira retorna-la sem os caracteres de pontuação
    str->str
    """
    novastr=''
    if ',' in string:
        novastr = str.replace(string,',',' ')
        string = novastr
        
    if '?' in string:
        novastr = str.replace(string, '?', ' ')
        string = novastr
        
    if '.' in string :
        novastr = str.replace(string, '.',' ')
        string= novastr
        
    if '-' in string:
        novastr= str.replace(string, '-', ' ' )
        string = novastr
        
    if ';' in string:
        novastr= str.replace(string, ';' , ' ')
        string = novastr
        
    if ':' in string:
        novastr= str.replace(string, ':',' ' )
        string = novastr
        
    if '!' in string:
        novastr = str.replace(string, '!' , ' ')
        string = novastr

    return novastr




def inverte(frase):
    frase = str.lower(retira_pontuacao(frase))
    return frase