from tkinter import * # Importando biblioteca gráfica

expression = "" # Declarando variavel do valor atual
btn_color = "cyan" # cor do botao
win_color = "light gray" # cor da janela
txt_color = "black" # cor dos texto
btn_width = 12
btn_height = 2

# Funcao que atualiza o valor no leitor
def press(num):
	# aponta para o valor atual
	global expression

	# adiciona o valor inserido ao valor atual
	expression = expression + str(num)

	# atualiza o valor pelo metodo set
	equation.set(expression)


# Funcao que valida a expressao atual
def equalpress():
	# Tenta validar, exibe "error" caso aconteça

	try:

		global expression

		# realiza os calculos e converte o resultado para str
		total = str(eval(expression))

		equation.set(total)

		# inicia o valor do visor como vazio
		expression = ""

	 # caso tenha algum erro no processo irá exibir erro
	 # e mudar o valor para vazio
	except:

		equation.set(" error ")
		expression = ""


# Funcao que limpa o valor do visor

def clear():
	global expression
	expression = ""
	equation.set("")


# Finalmente o código principal da calculadora
if __name__ == "__main__":
	# Cria uma janela com o Tkinter
	# a variavel gui e um acronimo para "Graphical user interface"
	gui = Tk()

	# Define a cor de fundo da janela
	gui.configure(background=win_color)

	# Define o nome da janela
	gui.title("Calculadora em Python")

	# Define as dimensões da janela
	gui.geometry("376x220")

	# Instanciando uma classe str
	equation = StringVar()

	# Criando o campo do valor atual
	expression_field = Entry(gui, textvariable=equation)

	# O metodo grid e usado para posicionar objetos
	# conforme a posicao na documentacao da biblioteca
	expression_field.grid(columnspan=40, ipadx=125)

	# Cria, posiciona e atribui cores e funcoes aos botoes
	button1 = Button(gui, text=' 1 ', fg=txt_color, bg=btn_color,
					command=lambda: press(1), height=btn_height, width=btn_width)
	button1.grid(row=2, column=0)

	button2 = Button(gui, text=' 2 ', fg=txt_color, bg=btn_color,
					command=lambda: press(2), height=btn_height, width=btn_width)
	button2.grid(row=2, column=1)

	button3 = Button(gui, text=' 3 ', fg=txt_color, bg=btn_color,
					command=lambda: press(3), height=btn_height, width=btn_width)
	button3.grid(row=2, column=2)

	button4 = Button(gui, text=' 4 ', fg=txt_color, bg=btn_color,
					command=lambda: press(4), height=btn_height, width=btn_width)
	button4.grid(row=3, column=0)

	button5 = Button(gui, text=' 5 ', fg=txt_color, bg=btn_color,
					command=lambda: press(5), height=btn_height, width=btn_width)
	button5.grid(row=3, column=1)

	button6 = Button(gui, text=' 6 ', fg=txt_color, bg=btn_color,
					command=lambda: press(6), height=btn_height, width=btn_width)
	button6.grid(row=3, column=2)

	button7 = Button(gui, text=' 7 ', fg=txt_color, bg=btn_color,
					command=lambda: press(7), height=btn_height, width=btn_width)
	button7.grid(row=4, column=0)

	button8 = Button(gui, text=' 8 ', fg=txt_color, bg=btn_color,
					command=lambda: press(8), height=btn_height, width=btn_width)
	button8.grid(row=4, column=1)

	button9 = Button(gui, text=' 9 ', fg=txt_color, bg=btn_color,
					command=lambda: press(9), height=btn_height, width=btn_width)
	button9.grid(row=4, column=2)

	button0 = Button(gui, text=' 0 ', fg=txt_color, bg=btn_color,
					command=lambda: press(0), height=btn_height, width=btn_width)
	button0.grid(row=5, column=0)

	plus = Button(gui, text=' + ', fg=txt_color, bg=btn_color,
				command=lambda: press("+"), height=btn_height, width=btn_width)
	plus.grid(row=2, column=3)

	minus = Button(gui, text=' - ', fg=txt_color, bg=btn_color,
				command=lambda: press("-"), height=btn_height, width=btn_width)
	minus.grid(row=3, column=3)

	multiply = Button(gui, text=' * ', fg=txt_color, bg=btn_color,
					command=lambda: press("*"), height=btn_height, width=btn_width)
	multiply.grid(row=4, column=3)

	divide = Button(gui, text=' / ', fg=txt_color, bg=btn_color,
					command=lambda: press("/"), height=btn_height, width=btn_width)
	divide.grid(row=5, column=3)

	equal = Button(gui, text=' = ', fg=txt_color, bg=btn_color,
				command=equalpress, height=btn_height, width=btn_width)
	equal.grid(row=5, column=2)

	clear = Button(gui, text='Clear', fg=txt_color, bg=btn_color,
				command=clear, height=btn_height, width=btn_width)
	clear.grid(row=5, column='1')

	Decimal= Button(gui, text='.', fg=txt_color, bg=btn_color,
					command=lambda: press('.'), height=btn_height, width=btn_width)
	Decimal.grid(row=6, column=0)

	# Mantem a janela aberta em loop
	gui.mainloop()
