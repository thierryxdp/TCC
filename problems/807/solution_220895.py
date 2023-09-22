def conta_frases (f):
	"retornar o número de frases no texto de entrada f, sabendo que as frases são separadas pelas pontuações '!', '?', '...' e '.'"
    return f.count("!")+f.count("?")+f.count("...")+(f.count(".")-3*f.count("..."))