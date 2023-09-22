def lingua_p(palavra):
    """Função que recebe como parâmetro e retorna a mesma palavra traduzida para a língua do P."""
    """str->str"""
    palavratrad=""
    for x in palavra:
        if str.lower(x) not in 'bcdfghjklmnpqrstvwxyzç':
            palavratrad+=x+'p'+x
            else:
                palavratrad+=x
    return str.lower(palavratrad)