def inverte(frase):
    igualar=frase.lower()
    conserto1=igualar.replace('!','.')
    conserto2=conserto1.replace('?','.')
    conserto3=conserto2.replace('...','.')
    conserto4=conserto3.replace(':','.')
    conserto5=conserto4.replace(';','.')
    conserto6=conserto5.replace('-','.')
    conserto7=conserto6.replace(',','.')
    lista=conserto7.split('.')
    lista_separada=(' '.join(lista).split)()
    invertida=lista_separada[::-1]
    return ' '.join(invertida)