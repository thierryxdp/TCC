def uppCons(frase):
    'dado uma frase, retorna essa frase com suas consoantes em maiusculo'
    frase=list(frase)
    i=0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiouÁÉÍÓÚáéíóúÃÕãõÂÊÎÔÛâêîôûÀÈÌÒÙàèìòù':
            frase[i]=str.upper(frase[i])
        i+=1
    frase=str.join('',frase)
    return frase