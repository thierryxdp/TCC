def uppCons(frase):
    """funcao que recebe uma frase e retorna a frase com as consoantes em caixa alta"""
    """str->str"""
    i = 0
    frasenova=''
    while i < len(frase):
        if frase[i] in 'aeiou':
            frasenova = frasenova + frase[i]
        else:
        	frasenova = frasenova + str.upper(frase[i])
        i = i + 1
        
        return frasenova