# Passo 1 : Entrar no sistema/site da empresa
# Passo 2 : Clica no botão de login
# Passo 3 : Abrir a base de dados
# Passo 4 : Cadastrar os produtos/clientes
#dadosPas so 5 : Gerar repetir o passo 4 até o final da base de dados
# Dica : digite no goolge pyautogui para aprender mais sobre a biblioteca e suas funcionalidades.

import pyautogui
import time
pyautogui.click # Clica em um local específico da tela
pyautogui.write # Escreve um texto
pyautogui.press # Pressiona uma tecla           
pyautogui.hotkey # Pressiona uma combinação de teclas

pyautogui.PAUSE = 1 # Define uma pausa de 1 segundo entre as ações para evitar que o script execute muito rápido
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Váriavel que armazena o link do site


# Passo 1 :Abrir o navegador e acessar o site

pyautogui.press('win') # Pressiona a tecla Windows
pyautogui.write('edge') # Escreve "edge" para procurar o navegador
pyautogui.press('enter') # Pressiona Enter para abrir o navegador
pyautogui.write(link) # Escreve o endereço do site
pyautogui.press('enter') # Pressiona Enter para acessar o site

time.sleep(2) # Aguarda 2 segundos para o site carregar

# Passo 2 : Clica no botão de login e realizar o login

pyautogui.click(x=913, y=402) # Clica no botão de login (substitua as coordenadas pelos valores corretos) E USAR ZOOM 100% PARA MELHOR PRECISÃO
pyautogui.write('joao') # Escreve o nome de usuário
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o campo de senha
pyautogui.write('123456') # Escreve a senha
pyautogui.press('enter') # Pressiona Enter para realizar o login

time.sleep(2) # Aguarda 2 segundos para o login ser processado e a próxima página carregar

# Passo 3 : Abrir a base de dados(importar o arquivo excel)

import pandas
tabela = pandas.read_csv("produtos.csv") # Lê o arquivo CSV e armazena em uma variável chamada "tabela"

# Passo 4 : Cadastrar os produtos/clientes e colocar para repetir

#codigo
pyautogui.click(x=887, y=285) # Clica no campo de código do produto (substitua as coordenadas pelos valores corretos)
pyautogui.write("MOLO000251") # Escreve o código do produto
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o próximo campo

#marca
pyautogui.write("Logitech") # Escreve a marca do produto
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o próximo campo

#tipo
pyautogui.write("Mouse") # Escreve o tipo do produto
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o próximo   

#categoria 
pyautogui.write("1") # Escreve a categoria do produto
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o próximo

#preço unitário
pyautogui.write("25.95") # Escreve o preço unitário do produto
pyautogui.press('tab') # Pressiona a tecla Tab para ir para o próximo

#custo do produto
pyautogui.write("6.5") # Escreve o custo do produto
pyautogui.press("tab") # Pressiona Enter para salvar o cadastro do produto

#OBS
pyautogui.write("NaN")# Escreve a observação do produto (se houver)
pyautogui.press("enter")# Pressiona Enter para salvar o cadastro do produto

#Passo 5 repetir o passo 4 para os próximos produtos da base de dados