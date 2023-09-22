def lingua_p(palavra):
    "Função que traduz a palavra de entrada para a lingua do p. str --> str"
    menor=str.lower(palavra)
    nova=''
    for  letra in menor:
        if letra in 'AÃÂÁÀEÉÈÊIÍÌÎOÓÒÕÔUÚÙÛaãâáàeêéèiîíìoõôóòuûúù':
            nova=nova+letra+'p'+letra
        else:
            nova=nova+letra
    return nova