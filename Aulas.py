# # Aula 7
# from selenium import webdriver
#
# chrome = webdriver.Chrome()         # Abre Chrome.
# chrome.get('http://google.com')     # Entra na página informada.

# # Aula 8
# from whatsapp_api import WhatsApp
#
# contato = 'Supositório filosófico'
#
# wp = WhatsApp()             # Abre Chrome já na página do WhatsApp Web.
# wp.search_contact(contato)  # Procura por nome ou número do contato (ou nome do grupo). Se houver homônimos, retorna o primeiro.
# wp.get_group_numbers()

# Construindo o bot (aulas 11 a 15)
from time import sleep
from whatsapp_api import WhatsApp

contato = 'Eu mesmo'
mensagem = "Olá! Sou um bot!"

wp = WhatsApp()             # Abre Chrome já na página do WhatsApp Web.

input('Pressione enter após QR code')

nomes_palavras_chave = []


wp.search_contact(contato)

wp.send_message(mensagem)


print('Fechando chrome em:')
for i in range(10):
    sleep(1)
    print(10 - i)
wp.driver.close()           # Fecha o Chrome.