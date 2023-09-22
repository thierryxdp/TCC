def lingua_p(frase):
    vogaisTodas='AEIOUaeiouáéíóúâêîôû'
    resultadoP=''
    for index in frase:
            if index in vogaisTodas:
                resultadoP+='p'+ index
    return resultadoP