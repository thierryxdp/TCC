def lingua_p(palavra):
    """Função que recebe como entrada uma palavra em formato de string, 
    e retorna a mesma palavra traduzida na lingua do P;
    str-->str"""
    mini = str.lower(palavra)
    traducao = ''
    for i in palavra:
        if i in 'aeiouáâãéêóôú':
            traducao = traducao + i + 'p' + i
        elif i in 'bcdfghjklmnpqrstvwxyzç':
            traducao = traducao + i
    return traducao