def conta_frase(fras,palav,pos):
    '''função que transforma uma palavra identificada na frase em caixa alta, e, caso ela não exista, ela será inserida na posição desejada
	str,str,int -> str'''
    separado = fras.split()
    if palav in separado:
        repet = separado.index(palav)
        separado[repet] = str.upper(palav)
        return str.join(' ',separado)
    else:
        list.insert(separado,pos,palav)
        alterada = str.join(' ',separado)
        return conta_frase