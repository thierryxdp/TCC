def conta_frases (f):
    return f.count("!")+f.count("?")+f.count("...")+(f.count(".")-3*f.count("..."))