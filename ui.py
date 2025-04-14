import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Jogo do Silvio Santos")
root.geometry('800x900')

# Perguntas e respostas
perguntas = [
    {
        "pergunta": "Quem foi que descobriu o Brasil?",
        "opcoes": [
            ("(a) Dom Pedro Primeiro", "a"),
            ("(b) Dom Pedro I", "b"),
            ("(c) Pedro Álvares Cabral", "c"),
            ("(d) Marechal Deodoro", "d")
        ],
        "correta": "c"
    },
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": [
            ("(a) Londres", "a"),
            ("(b) Paris", "b"),
            ("(c) Roma", "c"),
            ("(d) Berlim", "d")
        ],
        "correta": "b"
    },
    {
        "pergunta": "Quando o Brasil venceu o penta?",
        "opcoes": [
            ("(a) 1994", "a"),
            ("(b) 1998", "b"),
            ("(c) 2002", "c"),
            ("(d) 2006", "d")
        ],
        "correta": "c"
    }
]

indice_pergunta = 0
resposta_var = tk.StringVar()
botoes = []

def mostrar_pergunta():
    global botoes
    resposta_var.set("")
    pergunta_atual = perguntas[indice_pergunta]
    
    pergunta_label.config(text=pergunta_atual["pergunta"])
    
    for i, (texto, valor) in enumerate(pergunta_atual["opcoes"]):
        botoes[i][0].config(text=texto, value=valor, bg="white", fg="black")
        botoes[i] = (botoes[i][0], valor)  # Atualiza valor no botão

def verificar_resposta():
    global indice_pergunta
    resposta = resposta_var.get()
    correta = perguntas[indice_pergunta]["correta"]

    if resposta == "":
        messagebox.showwarning("Aviso", "Escolha uma opção antes de verificar!")
        return

    for botao, valor in botoes:
        if valor == correta:
            botao.config(fg="white", bg="green")
        elif valor == resposta:
            botao.config(fg="white", bg="red")

    if resposta == correta:
        messagebox.showinfo("Resultado", "Acertou! Parabéns 😄")
    else:
        messagebox.showerror("Resultado", "Errou! Tente novamente 😢")

    indice_pergunta += 1
    if indice_pergunta < len(perguntas):
        root.after(2000, mostrar_pergunta)
    else:
        messagebox.showinfo("Fim do Quiz", "Você concluiu o quiz!")
        botao_verificar.config(state="disabled")

# Interface
assunto = tk.Label(root, text="Bem-vindo ao meu quiz", font=("Arial", 30))
assunto.grid(row=0, column=0, columnspan=2, pady=20)

pergunta_label = tk.Label(root, text="", font=('Arial', 18), anchor="w")
pergunta_label.grid(row=1, column=0, columnspan=2, pady=20, sticky="w")

# Radiobuttons
for i in range(4):
    botao = tk.Radiobutton(root, text="", font=('Arial', 16), variable=resposta_var,
                           value="", anchor="w", bg="white", fg="black")
    botao.grid(row=2+i, column=0, columnspan=2, pady=10, sticky="w")
    botoes.append((botao, ""))

botao_verificar = tk.Button(root, text="Verificar", font=('Arial', 16), command=verificar_resposta)
botao_verificar.grid(row=6, column=0, columnspan=2, pady=30)

mostrar_pergunta()
root.mainloop()
