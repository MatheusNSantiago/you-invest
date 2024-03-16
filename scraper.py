from newspaper import Article
from typing import Literal


# import nltk
# nltk.download('punkt')

Categoria = Literal["criptomoedas", "agro", "exterior"]
class Artigo:

    def __init__(self, url):
        self.url = url
        self.article = Article(self.url)
        self.article.download()
        self.article.parse()

        self.titulo = self.article.title
        self.data = self.article.publish_date
        self.texto = self.article.text
        self.capa = self.article.top_image
