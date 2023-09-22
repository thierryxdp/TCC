def retira_pontuacao(string):
    '''Substitui todos os caracteres de pontuação
       ('—', ',', ':', ';', '.', '!', '?', '...')
       de uma frase por espaço;
       str -> str'''
    a = string.replace('—', ' ')
    b = a.replace(',', ' ')
    c = b.replace(': ', ' ')
    d = c.replace('; ', ' ')
    e = d.replace('... ', ' ')
    f = e.replace('! ', ' ')
    g = f.replace('? ', ' ')
    h = g.replace('. ', ' ')
    i = h.replace('.', ' ')
    j = i.replace('!', ' ')
    k = j.replace('?', ' ')
    l = k.replace('-', ' ')
    return l
def inverte(string):
    '''Dada uma frase, retorna outra com as mesmas palavras
       na ordem inversa, sem letras maiúsculas e sem a pontuação;
       str -> str'''
    string_1 = funcao3(string)
    string_2 = string_1.strip()
    string_3 = string_2.lower()
    string_4 = string_3.split()
    string_4.reverse()
    string_5 = str.join(' ', string_4)
    return string_5