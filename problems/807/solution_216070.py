def conta_frases(frases):
    f1= frases.count(".")
    f2= frases.count("!")
    f3= frases.count("?")
    f4= frases.count("...")
    return (f1-(3*f4))+f2+f3+f4