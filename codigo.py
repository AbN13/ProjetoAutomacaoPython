# Passo 1: Entrar no sistema da empresa;
# Passo 2: Fazer login;
# Passo 3: Pegar/Importar a base de dados;
# Passo 4: Cadastrar um produto;
# Passo 5: Repetir o processo(passo 4) de cadastro até cadastrar todos produtos;
# pip install pyautogui
# pip install pandas openpyxl numpy
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - pressionar 1 tecla
# pyautogui.hotkey - combinar teclas ( Ctrl+C)
# pyautogui.scroll - dar scroll na tela (rolar a tela pra cima e pra baixo)
# pausar 0.5 segundos entre cada comando
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa 
# abrir o navegador 
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter") 

# entrar no link

pyautogui.click(x=195, y=64)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Passo 2: fazer login
# clicar no campo de email
pyautogui.click(x=389, y=407)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("work.abn96@gmail.com")

#passar para o campo senha
pyautogui.press("tab")
pyautogui.write("abnzika")
pyautogui.click (x=673, y=571)

time.sleep(3)

#passo 3 - importar banco de dados 
tabela = pd.read_csv("Produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
#codigo
    pyautogui.click(x=656, y=337)
    tabela.loc[linha, "codigo"]
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

#marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

# tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)
  
# categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

# preço unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

# custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

# obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": 
        pyautogui.write(obs)

# clicar no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir para todos os produtos - para todas as linhas da tabela






