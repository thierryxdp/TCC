# Dado um texto em uma string, queremos saber quantas frases
# ele possui.
# Resolução:
# 1. Aplica a função strip a fim de retirar quaisquer espaços
#    inicial ou final;
# 2. Troca a pontuação que marca o fim de uma frase por 
#    tralha através da função str.replace;
# 3. Repita o processo para todas as pontuações, passando a
#    cada nova vez o resultado anterior como argumento da função;
# 4. Separe a string final nas tralhas usando a função str.split;
# 5. Aplique a função len ao resultado acima e diminua um
#    (a fim de evitar a contagem de um elemento vazio)
# str ->  int

def conta_frases(texto):
    '''Dado um texto em uma string, queremos saber quantas
    frases ele possui; 
    str ->  int'''
    s_esp = str.strip(frase)
    s_exclam = str.replace(s_esp, '!', '#')
    s_retic = str.replace(s_exclam, '...', '#')
    s_ponto = str.replace(s_retic, '.', '#')
    s_interrog = str.replace(s_ponto, '?', '#')
    list_frases =  str.split(s_interrog, '#')
    quantfrases = len(list_frases) - 1
    return quantfrases