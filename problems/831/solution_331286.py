def lingua_p(p):
    '''
    Recebe uma palavra (p) qualquer. Torna-a minúscula.
    Declara uma variável com todas as possíveis vogais.
    [Se tem algum método que ele leia as vogais sem ter
    que declarar todos os acentos possíveis, me informe!]
    Declara uma variável (t) com um texto vazio. Corre todas
 	Corre todas as letras (l) de p e verifica se esta letra
    é uma vogal. Se for, repete o texto até essa letra e
    adiciona o "p" e mais essa mesma letra. Por fim, retorna
    a palavra traduzida (t).
    
    '''
    p = p.lower(); v = "aeiouáéíóú"; t = ''
    for l in p:
        if l in v: t = t+l+'p'+l
        else: t = t+l
    return t