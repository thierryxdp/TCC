# Dada uma frase, retorna suas palavras descapitalizadas
# na ordem inversa e sem pontuação;
# str -> str
# Resolução:
# 1. Reaproveita o algoritmo que retira pontuação e o aplica;
# 2. À string obtida, aplica str.lower para tornar todas as
#    letras minúsculas;
# 3. Aplica str.split para separar a frase nos espaços 
#    e torná-la uma lista;
# 4. Pega o intervalo da lista de trás pra frente, para inverter
#    a ordem de seus elementos;
# 5. Aplica str.join usando espaços como separador a fim de
#    transformar a lista em string;
# 6. Devolve

def retira_pontuacao(frase):
    '''Dada uma frase, queremos substituir toda sua 
    pontuação por espaços;
    str -> str'''
    trav = str.replace(frase, '—', ' ')
    virg = str.replace(trav, ',', ' ')
    doispt = str.replace(virg, ':', ' ')
    ptvirg = str.replace(doispt, ';', ' ')
    ret = str.replace(ptvirg, '...', ' ')
    ponto = str.replace(ret, '.', ' ')
    interrog = str.replace(ponto, '?', ' ')
    exclam = str.replace(interrog, '!', ' ')
    hifen = str.replace(exclam, '-', ' ')
    frasefinal = hifen
    return frasefinal

def inverte(frase):
    '''Dada uma frase, retorna suas palavras descapitalizadas
    na ordem inversa e sem pontuação;
    str -> str'''
    s_pontuac = retira_pontuacao(frase)
    s_maiusc = str.lower(s_pontuac)
    lista = str.split(s_maiusc)
    invert_lista = lista[::-1]
    novafrase = str.join(' ', invert_lista)
    return novafrase