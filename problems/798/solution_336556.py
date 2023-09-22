def freq_palavras(frases):
    ''' Função que recebe de entrada um texto (string) e 
    retorna um dicionario relacionando cada palavra a 
    quantidade de vezes que ela aparece nesse texto, em que 
    cada palavra eh a chave e a quantidade, o valor.
    str -> dict'''
    s = str.split(frases)
    dict_ret = {}
    for palavra in s:
        dict_ret[palavra] = list.count(s,palavra)
    return dict_ret

#Casos de teste freq_palavras('para somar e multiplicar nao 
# importa a ordem dos valores. a mudanca na ordem nao afeta 
#o resultado') ==
# {'para': 1, 'somar': 1, 'e': 1, 'multiplicar': 1, 'nao': 2,
# 'importa': 1, 'a': 2, 'ordem': 2, 'dos': 1, 'valores.': 1,
# 'mudanca': 1, 'na': 1, 'afeta': 1, 'o': 1, 'resultado': 1}

# freq_palavras('sol e areia, mar e brisa, praia eh tudo de 
# bom') == 
# {'sol': 1, 'e': 2, 'areia,': 1, 'mar': 1, 'brisa,': 1, 
# 'praia': 1,'eh': 1, 'tudo': 1, 'de': 1, 'bom': 1}