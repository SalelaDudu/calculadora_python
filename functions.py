# Função que atualização a expressão
def press(num):

  global expressao
  # Adiociona o input do usuário ao valor já existente
  expressao = expressao + str(num)

# Função que calcula a expressão atual
def equalpress():
  # Tenta realizar a operação e retorna erro caso falhe
  try:
    global expressao

    total =str(eval(expressao))
    expressao = ""

  except:
    expressao = "Error"  
# Função que limpa a memória da calculadora
def clear():
  
  global expressao
  expressao = ""

