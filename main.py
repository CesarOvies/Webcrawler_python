from bs4 import BeautifulSoup
import requests
import re

#adione a página em questão.
url = 'https://www.magazineluiza.com.br/xbox-series-s-2020-nova-geracao-512gb-ssd-1-controle-branco-microsoft-lancamento/p/043083000/ga/otga/'

#tras a página para dentro da variavel url
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#procura o nome do produto pela classe:
produto = soup.find(class_={"header-product__title"})
#produto = soup.find(class_={"header-product"}, string={("fullTitle")})

#procura a url do produto pela classe:
urlimagem = soup.find(class_={"showcase-product__container-img"})
#urlimagem = soup.find(class_={"header-product}, string={("imageUrl")})

#procura o preço do produto pela classe:
preco = soup.find(class_={"price-template__text"})
#preco = soup.find(class_={"header-product"}, string={("pricetemplate")})

#procura o estoque do produto pela classe:
estoque = soup.find(class_={"header-product"}, string={"installmentQuantity"})

#procura a url do produto pelo tag rel(relação):
urlproduto = soup.find(rel={"alternate"})

#joga na tela as informações buscadas anteriormente
print("nome do produto: ", produto)
print("Url da imagem: ", urlimagem)
print("preço: ", preco)
print("Disponibilidade: ", estoque)
print("Url produto", urlproduto)

#abaixo fiz de uma outra forma buscando todas as informações.
#trazendo todas as informações, funcional em qualquer link do magalu.
#inf= soup.find(string=re.compile("productData"))
#print("informações: ", inf)



