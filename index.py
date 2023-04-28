import tkinter as tk

def decimal_para_binario(decimal):
    # Divide o número em sua parte inteira e fracionária
    inteira, fracionaria = str(decimal).split('.')
    
    # Converte a parte inteira para binário
    binario_inteiro = bin(int(inteira))[2:]
    
    # Inicializa a parte fracionária em 0
    binario_fracionario = ''
    
    # Converte a parte fracionária para binário
    fracionaria = float('0.' + fracionaria)
    while fracionaria > 0:
        # Multiplica a parte fracionária por 2
        fracionaria *= 2
        
        # Se a parte inteira for maior ou igual a 1, adiciona 1 ao binário e subtrai 1 da parte inteira
        if int(fracionaria) >= 1:
            binario_fracionario += '1'
            fracionaria -= 1
        # Senão, adiciona 0 ao binário
        else:
            binario_fracionario += '0'
    
    # Retorna o número em binário completo
    return binario_inteiro + '.' + binario_fracionario


def binario_para_decimal(binario):
    # Divide o número binário em sua parte inteira e fracionária
    inteira, fracionaria = binario.split('.')
    
    # Converte a parte inteira para decimal
    decimal_inteiro = int(inteira, 2)
    
    # Converte a parte fracionária para decimal
    decimal_fracionario = sum(int(digit) * 2 ** -(i+1) for i, digit in enumerate(fracionaria))
    
    # Soma as duas partes e retorna o resultado
    return decimal_inteiro + decimal_fracionario


def calcular():
    if opcao.get() == 1:
        resultado.set(decimal_para_binario(float(num.get())))
    elif opcao.get() == 2:
        resultado.set(binario_para_decimal(num.get()))

# Cria a janela
janela = tk.Tk()
janela.title("Conversor Decimal-Binário")
janela.resizable(False, False)
janela.configure(bg='#FFF')

# Cria os widgets
tk.Label(janela, text="Conversor Decimal-Binário", font=("Arial", 18), bg='#FFF').grid(row=0, column=0, columnspan=2, pady=10)

opcao = tk.IntVar()
tk.Radiobutton(janela, text="Decimal para binário", variable=opcao, value=1, bg='#FFF').grid(row=1, column=0, pady=10, padx=10)
tk.Radiobutton(janela, text="Binário para decimal", variable=opcao, value=2, bg='#FFF').grid(row=1, column=1, pady=10, padx=10)

tk.Label(janela, text="Número:", bg='#FFF').grid(row=2, column=0, pady=10, padx=10)
num = tk.Entry(janela, borderwidth=2, relief="groove")
num.grid(row=2, column=1)

resultado = tk.StringVar()
tk.Label(janela, text="Resultado:", bg='#FFF').grid(row=3, column=0, pady=10, padx=10)
tk.Label(janela, textvariable=resultado, bg='#FFF').grid(row=3, column=1)

copiar = tk.Button(janela, text="Copiar resultado", bg='#00bfff', fg='#FFF', command=lambda: janela.clipboard_append(resultado.get()))
copiar.grid(row=4, column=1, pady=10)

tk.Button(janela, text="Calcular", bg='#00bfff', fg='#FFF', command=calcular).grid(row=4, column=0, pady=10, padx=10)

# cria o objeto de imagem a partir do arquivo


# cria o label para exibir a imagem


# Inicia o loop da janela
janela.mainloop()