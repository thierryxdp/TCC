def retira_pontuacao(frase):

    #o codigo funciona por etapas
# o comando split separa a frase em strs baseando no caracter separador
# o comando join junta as strings separadas e adiona o caracter desejado
# entre elas, no caso ' ' espaço. então novamente a frase vai para
# split e ela separa com base em outro caracter separador..
    frase = str.split(frase,'-')
    frase = str.join(' ',frase)
    frase = str.split(frase,',')
    frase = str.join(' ',frase)
    frase = str.split(frase,':')
    frase = str.join(' ',frase)
    frase = str.split(frase,'?')
    frase = str.join(' ',frase)
    frase = str.split(frase,'.')
    frase = str.join(' ',frase)
    return frase