def lingua_p(palavra):
    for i in palavra:
        vogais = 'AEIOUaeiouÁÉÍÓÚáéíóúÂÊÎÔÛâêîôûÃÕãõ'
        if i in vogais:
            palavra = palavra.replace(i,i+ "p" +i)
            i=+2
        else: i=+1
    return palavra