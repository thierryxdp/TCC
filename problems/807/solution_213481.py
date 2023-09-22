def conta_frases(texto):
    "."=!"..."
    s=str(texto)
    return int(str.count(s,"!"))+int(str.count(s,"?"))+int(str.count(s,"."))+int(str.count(s,"..."))