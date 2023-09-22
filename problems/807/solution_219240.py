def conta_frases(frases):
    n_frases= frases.count("!") + frases.count("?") + frases.count("...") + frases.count(".") - 3 * frases.count("...")
    return n_frases