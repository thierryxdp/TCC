def lingua_p(string):
    '''funcao que retorna a palavra dada como entrada traduzida para a lingua do P
    str->str'''
    vogais = ['a','e','i','o','u','A','E','I','O','U','á','é','i','ó','ú', 'Á', 'É','Í','Ó','Ú']
    traducao=''
    for i in string:
        if i in vogais:
            i=i+'p'+i
        traducao=traducao+i 
    return traducao