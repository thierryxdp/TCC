def hashtag(s):
        """Adiciona 3 hashtags uma no inicio da string uma no meio
e a ultima no final.Entra string desejada(s). str->str"""
        return '#'+s[0:len(s)//2]+'#'+s[len(s)//2:]+'#'