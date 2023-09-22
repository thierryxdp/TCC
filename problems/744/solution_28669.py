# Dada uma string, queremos uma nova string formada pela anterior
# acrescida do caractere "#" em seu início, meio e final.
# Resolução:
# 1. Concatenar um "#" à esquerda da string;
# 2. Concatenar um "#" à direita da string obtida acima;
# 3. Se a string obtida em (2) tiver número par de caracteres:
# 3.1 Dividí-la em duas metades iguais;
# 3.2 Concatenar "#" à direita da primeira metade;
# 3.3 Concatenar a segunda metade à direita da string acima obtida;
# 3.4 Devolver.
# 4. Se a string obtida em (2) tiver número ímpar de caracteres:
# 4.1 Dividí-la em duas partes tal que a segunda parte tenha um 
#     elemento a mais;
# 4.2 Concatenar "#" à direita da primeira metade;
# 4.3 Concatenar a segunda metade à direita da string acima obtida;
# 4.4 Devolver.

# str-> str

def hashtag(s):
    '''Dada uma string, queremos uma nova string formada pela anterior
    acrescida do caractere "#" em seu início, meio e final;
    str -> str'''
    stralha = "#" + s + "#"
    if len(stralha) % 2 == 0:
        return stralha[: (len(stralha) // 2)] + "#" + stralha[(len(stralha) // 2) :]
    else:
        return stralha[: (len(stralha) // 2)] + "#" + stralha[(len(stralha) // 2) :]