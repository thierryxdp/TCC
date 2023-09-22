def conta_frase(texto):
    "Função que dar um texto e retorna o  numero de frases existentes nesse texto dados uns determinados parametros"
    y=str.replace(texto,"...","#")
    return str.count(y,".")+str.count(y,"!")+str.count(y,"?")+str.count(y,"#")