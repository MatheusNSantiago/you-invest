from faz_os_treco import faz_treco_la_de_resumir
from render import render
from scraper import Artigo
import webbrowser

url = "https://finance.yahoo.com/news/el-salvador-thousands-more-bitcoins-004326888.html#:~:text=El%20Salvador%20moved%20more%20than,stash%20of%20the%20digital%20asset"

artigo = Artigo(url)
artigo_resumido = faz_treco_la_de_resumir(artigo)
render(artigo_resumido)

webbrowser.open("index.html")

