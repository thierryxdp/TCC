def inverte(string):
    "Função que recebe uma string e retorna a mesma de modo invertido."
    string = string.lower()
    especias = ['!','?','#','$','@','%','&','*',',','.','-']
    for testar in especias:
        if testar != '-' and testar in string:
            string = string.replace(testar,'')
        else:
            string = string.replace(testar,' ')
    string = string.split()
    string.reverse()
    string = ' '.join(string)
    return string