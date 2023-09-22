def lingua_p(palavra):
    """A função recebe uma palavra e retorna a mesma, inserindo um p à 
    frente de cada vogal e repetindo essa mesma vogal após o p. Além disso, 
    ignora a diferença entre maiscula e minuscula, retornando toda a palavra em
    em minuscula;
    str -> str"""
    nova_palavra = ''
    for i in range(len(palavra)):
        if palavra[i] in 'AEIOUaeiouÁÀÃÂÉÊÕÓÔÚÍáàãâéêôõóúí':
            nova_palavra += palavra[i]+'p'+palavra[i]
        else:
            nova_palavra += palavra[i]
    return str.lower(nova_palavra)