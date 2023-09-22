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
    """
    Essa função dado uma frase como argumento ira retorna-la com as letras
    em minusculas sem a pontuação e na ordem inversa
    str->str
    """
    
    nova_frase=''
    nova_frase= str.lower(retira_pontuacao(frase))
    lista = str.split(nova_frase)
    lista = lista[::-1]
    nova_frase = str.join(nova_frase,lista)
    
    return nova_frase