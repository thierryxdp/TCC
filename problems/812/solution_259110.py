# Dada uma frase, queremos substituir toda sua pontuação
# por espaços.
# str -> str
# Resolução:
# 1. Utiliza a função str.replace a fim de trocar o travessão
#    por espaço;
# 2. Repita o processo para todas as pontuações utilizando sempre
#    como argumento da nova função a saída da última;
# 3. Devolva

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