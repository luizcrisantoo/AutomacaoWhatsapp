from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# lista de contatos e mensagens
contatos = ['testandocodigo']
mensagens = ['Olá, [nome]! estou testando o programa?']

# iniciar o navegador
driver = webdriver.Chrome()

# abrir o WhatsApp Web
driver.get('https://web.whatsapp.com/')

# aguardar o usuário fazer login
input('Faça o login no WhatsApp Web e pressione Enter para continuar...')

# para cada contato e mensagem, enviar a mensagem
for contato, mensagem in zip(contatos, mensagens):
    # pesquisar o contato
    search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    search_box.send_keys(contato)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # substituir o [nome] na mensagem pelo nome do contato
    mensagem = mensagem.replace('[nome]', contato)

    # digitar a mensagem e enviar
    input_box = driver.find_element_by_xpath('//div[contains(@class,"_3Uu1_")]')
    input_box.send_keys(mensagem)
    input_box.send_keys(Keys.ENTER)
    time.sleep(2)

# fechar o navegador
driver.quit()
