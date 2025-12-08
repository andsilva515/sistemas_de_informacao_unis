import tkinter as tk
from tkinter import messagebox

# ----------------- Funções -----------------
def calcular_imc():
    try:
        altura_cm = float(entry_altura.get().replace(",", "."))
        peso = float(entry_peso.get().replace(",", "."))

        altura_m = altura_cm / 100
        imc = peso / (altura_m ** 2)

        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

        texto = (
            f"Paciente: {entry_nome.get()}\n"
            f"Endereço: {entry_endereco.get()}\n\n"
            f"Altura: {altura_cm:.1f} cm\n"
            f"Peso: {peso:.1f} kg\n\n"
            f"IMC: {imc:.2f}\n"
            f"Classificação: {classificacao}"
        )

        text_resultado.config(state="normal")
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, texto)
        text_resultado.config(state="disabled")

    except ValueError:
        messagebox.showerror("Erro", "Informe altura e peso válidos (números).")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    text_resultado.config(state="normal")
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, "Resultado")
    text_resultado.config(state="disabled")

def sair():
    janela.destroy()

# ----------------- Janela principal -----------------
janela = tk.Tk()
janela.title("Cálculo do IMC - Índice de Massa Corporal")
janela.resizable(False, False)
janela.geometry("600x260")

# ----------------- Linha 1: Nome -----------------
label_nome = tk.Label(janela, text="Nome do Paciente:")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry_nome = tk.Entry(janela, width=60)
entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# ----------------- Linha 2: Endereço -----------------
label_endereco = tk.Label(janela, text="Endereço Completo:")
label_endereco.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry_endereco = tk.Entry(janela, width=60)
entry_endereco.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# ----------------- Linha 3 e 4: Altura / Peso + Resultado -----------------
# --- Altura ---
label_altura = tk.Label(janela, text="Altura (cm)")
label_altura.grid(row=2, column=0, padx=10, pady=(5, 0), sticky="w")

entry_altura = tk.Entry(janela, width=15)
entry_altura.grid(row=2, column=0, padx=120, pady=(5, 0), sticky="w")

# --- Peso ---
label_peso = tk.Label(janela, text="Peso (Kg)")
label_peso.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

entry_peso = tk.Entry(janela, width=15)
entry_peso.grid(row=3, column=0, padx=120, pady=(10, 0), sticky="w")


# Caixa de resultado (ocupa mais espaço à direita)
text_resultado = tk.Text(janela, width=40, height=8)
text_resultado.grid(row=2, column=1, rowspan=2, padx=10, pady=5, sticky="w")
text_resultado.insert(tk.END, "Resultado")
text_resultado.config(state="disabled")

# ----------------- Linha inferior: botões -----------------
frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=4, column=0, columnspan=2, pady=15)

btn_calcular = tk.Button(frame_botoes, text="Calcular", width=15, command=calcular_imc)
btn_calcular.grid(row=0, column=0, padx=10)

btn_reiniciar = tk.Button(frame_botoes, text="Reiniciar", width=15, command=reiniciar)
btn_reiniciar.grid(row=0, column=1, padx=10)

btn_sair = tk.Button(frame_botoes, text="Sair", width=15, command=sair)
btn_sair.grid(row=0, column=2, padx=10)

janela.mainloop()
