def lingua_p(palavra):
    ''''''
    texto_minusculo = palavra.lower()
    if 'a' or 'e' or 'i' or 'o' or 'u' in texto_minusculo:
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