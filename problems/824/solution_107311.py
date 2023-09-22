def uppCons(frase):
    '''Função que recebe uma frase e a retorna com todas as suas consoantes em maiúsculo; str->str'''
    contador=0
    frasenova=''
    while contador<len(frase):
        if frase[contador] not in 'AEIOUaeiouÁÀÈÂÃÊÉÍÌÓÔÕUÚáàãâéèêíìóõôuú':
            consoante=str.upper(frase[contador])
            frasenova=frasenova+consoante
        else:
            frasenova=frasenova+frase[contador]
        contador = contador + 1
    return frasenova