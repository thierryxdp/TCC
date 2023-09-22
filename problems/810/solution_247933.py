def inverte(string):
    """Função que recebe uma string e recebe a mesma de modo invertido. 
    str > str"""
    string = string.lower()
    especiais = ['!', '?', '#', '$', '@', '%', '&', '*', ',','.','-']
    for testar in especiais:
        if testar != '-' and testar in string:
            string = string.replace(testar,'')
            else:
                string = string.replace(testar, ' ')
    string = string.split()
    string.reverse()
    string = ' '.join(string)
    return string