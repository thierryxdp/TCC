def lingua_p(texto_port):
    '''Função que, dado um texto qualquer escrito em 
português, retorna o mesmo texto traduzido para a língua 
do .
str --> str'''
    texto_minusculo = texto_port.lower()
    if 'aeiou' in texto_minusculo:
        lista_texto = list(texto_minusculo)
        frase_p = []
        for letra in lista_texto:
            if letra in 'aeiouáàéíóú':
                frase_p = frase_p + list(letra) + list('p') + list(letra)
            else:
                frase_p = frase_p + list(letra)
        frase_p = (''.join(frase_p))
        return frase_p
    else:
        return texto_minusculo