def lingua_p(palavra):
'''função que recebe como parâmetro uma palavra e retorna a mesma palavra traduzida para lingua do P; str->str'''
traduz=''
palavra = str.lower(palavra)
restricao = 'zxvcbnmçlkjhgfdsqwrtyp'
for i in range(len(palavra)):
    if palavra[i] not in restricao:
        traduz += palavra[i] + 'p' + palavra[i]
        else:
        traduz += palavra[i]
        return traduz