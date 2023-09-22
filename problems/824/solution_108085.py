def uppCons(frase):
    """
    Função que recebe uma string e retorna uma cópia
    com todas as suas consoantes em caixa alta
    
    str ---> str
    """
    
    nova_frase=''
    for i in frase:
        if  i.lower() in 'bcdfghjklmnpqrstvxwyzç':
            nova_frase += str(i).upper()
        else:
            nova_frase += str(i)
    return nova_frase