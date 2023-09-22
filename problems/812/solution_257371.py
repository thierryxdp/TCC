def retira(frase):

    pont = ["!","?",".",",",":","-",";","..."]

    for x in range(len(pont)):
        frase = frase.replace(pont[x],"")

    return frase