def retira_p(frase):
    for crc in frase:
        if crc in '.!,?:;-...':
            tira_tudo=str.replace(frase,crc,' ')
    return tira_tudo