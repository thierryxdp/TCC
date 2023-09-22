def retira_pontuacao(string):
    """
    Essa função apos receber uma string qualquer como argumento
    ira retorna-la sem os caracteres de pontuação
    str->str
    """
    
    if '.' in string:
        string = str.replace(string,'.',' ')
   
    elif '-' in string:
        string = str.replace(string,'-', ' ')
        
    elif ':' in string:
        string = str.replace(string,':', ' ')
        
    elif ';' in string:
        string = str.replace(string,';', ' ')
        
    elif ',' in string:
        string = str.replace(string,',', ' ')

    return string