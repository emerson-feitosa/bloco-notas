from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog



#criar uma lista com alguns títulos e colocar eles para abrirem aleatoriamente em uma pagina
# ou fazer com que os titulos abram de acordo com o dia ex bloco seguda, bloco terça
def nova_pagina():
    global numero_paginas_abertas
    numero_paginas_abertas += 1
    pagina = Tk()
    texto_pagina = Text(pagina, wrap="word", height=40, width=100, font="Arial 14")
    texto_pagina.pack()
    texto_na_pagina.append(texto_pagina)
    # dimensoes
    largura_total_pagina = pagina.winfo_screenwidth()
    altura_total_pagina = pagina.winfo_screenheight()
    largura_pagina = 800
    altura_pagina = 400
    posicao_eixo_xp = largura_total_pagina/2 - largura_pagina/2
    posicao_eixo_yp = altura_total_pagina/2 - altura_pagina/2
    pagina.geometry("%dx%d+%d+%d" % (largura_pagina, altura_pagina, posicao_eixo_xp, posicao_eixo_yp))
    pagina.resizable(FALSE, FALSE)
    #Menu
    menu_pagina = Menu(pagina)
    file_menu_pagina = Menu(menu_pagina, tearoff=0)
    menu_pagina.add_cascade(label="Arquivo", menu=file_menu_pagina)
    file_menu_pagina.add_command(label="Nova página", command=nova_pagina)
    file_menu_pagina.add_command(label="Abrir...", command=abrir_arquivo_pagina)
    file_menu_pagina.add_command(label="Salvar", command=salvar_arquivo_pagina)
    file_menu_pagina.add_command(label="Salvar como...", command=salvar_como_arquivo_pagina)
    file_menu_pagina.add_separator()
    file_menu_pagina.add_command(label="Sair", command=lambda: mensagens_pagina(pagina, texto_pagina))
    menu_pagina.add_command(label="Procurar", command=pesquisar_palavra_pagina)
    menu_pagina.add_command(label="Contador", command=contador)
    pagina.config(menu=menu_pagina)
    pagina.protocol("WM_DELETE_WINDOW", lambda: fechar_pagina(pagina, texto_pagina))




def abrir_arquivo_janela():
    global arquivo_atual_janela
    arquivo_janela = filedialog.askopenfilename(filetypes=(("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
    if arquivo_janela:
        arquivo_atual_janela = arquivo_janela
        with open(arquivo_janela, "r") as file_janela:
            conteudo = file_janela.read()
            texto_janela.delete("1.0", "end")
            texto_janela.insert("1.0", conteudo)

def salvar_arquivo_janela():
    global arquivo_atual_janela

    if arquivo_atual_janela:
        conteudo_janela = texto_janela.get("1.0", "end-1c")
        with open(arquivo_atual_janela, "w") as salvar:
            salvar.write(conteudo_janela)
    else:
        conteudo_janela = texto_janela.get("1.0", "end-1c")
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
        (("Arquivos de Texto", "*.txt"), ("Arquivos python", "*.py")))
        if arquivo:
            with open(arquivo, "w") as salvar:
                salvar.write(conteudo_janela)
                arquivo_atual_janela = arquivo

def salvar_como_arquivo_janela():
    conteudo_janela = texto_janela.get("1.0", "end-1c")
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
    (("Arquivos de Texto", "*.txt"), ("Arquivos python", "*.py")))
    if arquivo:
        with open(arquivo, "w") as salvar:
            salvar.write(conteudo_janela)


def pesquisar_palavra():
    palavra_pesquisada = simpledialog.askstring("Pesquisar", "Digite a palavra a ser pesquisada:")
    if palavra_pesquisada:
        texto = texto_janela.get("1.0", "end")
        texto_janela.tag_remove("destaque", "1.0", "end")
        posicao = texto.find(palavra_pesquisada)
        messagebox.showwarning("Aviso", f"Todas as plavras com: *{palavra_pesquisada}* foram destacadas")

        while posicao != -1:
            inicio = f"1.0+{posicao}c"
            fim = f"1.0+{posicao + len(palavra_pesquisada)}c"
            texto_janela.tag_add("destaque", inicio, fim)
            posicao = texto.find(palavra_pesquisada, posicao + 1)
        texto_janela.tag_config("destaque", background="green")



def abrir_arquivo_pagina():
    global arquivo_atual_pagina
    arquivo_pagina = filedialog.askopenfilename(filetypes=(("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
    if arquivo_pagina:
        arquivo_atual_pagina = arquivo_pagina
        with open(arquivo_pagina, "r") as file_pagina:
            conteudo = file_pagina.read()
            texto_na_pagina[-1].delete("1.0", "end")
            texto_na_pagina[-1].insert("1.0", conteudo)


def salvar_como_arquivo_pagina():
    conteudo_pagina = texto_na_pagina[-1].get("1.0", "end-1c")
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
    (("Arquivos de Texto", "*.txt"), ("Arquivos python", "*.py")))
    if arquivo:
        with open(arquivo, "w") as salvar:
            salvar.write(conteudo_pagina)


def salvar_arquivo_pagina():
    global arquivo_atual_pagina

    if arquivo_atual_pagina:
        conteudo_pagina = texto_na_pagina[-1].get("1.0", "end-1c")
        with open(arquivo_atual_pagina, "w") as salvar:
            salvar.write(conteudo_pagina)
    else:
        conteudo_pagina = texto_na_pagina[-1].get("1.0", "end-1c")
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
        (("Arquivos de Texto", "*.txt"), ("Arquivos python", "*.py")))
        if arquivo:
            with open(arquivo, "w") as salvar:
                salvar.write(conteudo_pagina)
                arquivo_atual_pagina = arquivo

def pesquisar_palavra_pagina():
    palavra_pesquisada = simpledialog.askstring("Pesquisar", "Digite a palavra a ser pesquisada:")
    if palavra_pesquisada:
        texto = texto_na_pagina[-1].get("1.0", "end")
        texto_na_pagina[-1].tag_remove("destaque", "1.0", "end")
        posicao = texto.find(palavra_pesquisada)
        messagebox.showwarning("Aviso", f"Todas as plavras com: *{palavra_pesquisada}* foram destacadas")
        while posicao != -1:
            inicio = f"1.0+{posicao}c"
            fim = f"1.0+{posicao + len(palavra_pesquisada)}c"
            texto_na_pagina[-1].tag_add("destaque", inicio, fim)
            posicao = texto.find(palavra_pesquisada, posicao + 1)
        texto_na_pagina[-1].tag_config("destaque", background="green")

def mensagens_pagina(pagina, texto_pagina):
    conteudo_pagina = texto_pagina.get("1.0", "end-1c")
    if conteudo_pagina != "":
        mensagem = messagebox.askyesno("Pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_pagina()
        else:
            pagina.destroy()
    else:
        pagina.destroy()


def mensagens_janela():
    conteudo_janela = texto_janela.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = messagebox.askyesno("Pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_janela()
        else:
            janela_bloco_notas.destroy()

    else:
        janela_bloco_notas.destroy()


def fechar_janela():
    conteudo_janela = texto_janela.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_janela()
            janela_bloco_notas.destroy()
        else:
            janela_bloco_notas.destroy()
    else:
        janela_bloco_notas.destroy()


def fechar_pagina(pagina, texto_pagina):
    conteudo_pagina = texto_pagina.get("1.0", "end-1c")
    if conteudo_pagina != "":
        mensagem = messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_pagina()
            pagina.destroy()
        else:
            pagina.destroy()
    else:
        pagina.destroy()

def contador():
    if numero_paginas_abertas == 1:
        messagebox.showinfo("Contador", f"Até o momento você criou {numero_paginas_abertas} nova anotação.")
    else:
        messagebox.showinfo("Contador", f"Até o momento você criou {numero_paginas_abertas} novas anotações.")




janela_bloco_notas = Tk()
arquivo_atual_janela = ""
arquivo_atual_pagina = ""
texto_na_pagina = []
numero_paginas_abertas = 1

texto_janela = Text(janela_bloco_notas, wrap="word", height=40, width=100, font="Arial 14")
texto_janela.pack()

# dimensoes
largura_total_janela = janela_bloco_notas.winfo_screenwidth()
altura_total_janela = janela_bloco_notas.winfo_screenheight()
largura_janela = 800
altura_janela = 400
posicao_eixo_x = largura_total_janela/2 - largura_janela/2
posicao_eixo_y = altura_total_janela/2 - altura_janela/2
janela_bloco_notas.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posicao_eixo_x, posicao_eixo_y))
janela_bloco_notas.resizable(FALSE, FALSE)
# Menu
menu_janela_bloco_notas = Menu(janela_bloco_notas)
file_menu_janela_bloco_notas = Menu(menu_janela_bloco_notas, tearoff=0)
menu_janela_bloco_notas.add_cascade(label="Arquivo", menu=file_menu_janela_bloco_notas)
file_menu_janela_bloco_notas.add_command(label="Nova página", command=nova_pagina)
file_menu_janela_bloco_notas.add_command(label="Abrir...", command=abrir_arquivo_janela)
file_menu_janela_bloco_notas.add_command(label="Salvar", command=salvar_arquivo_janela)
file_menu_janela_bloco_notas.add_command(label="Salvar como...", command=salvar_como_arquivo_janela)
file_menu_janela_bloco_notas.add_separator()
file_menu_janela_bloco_notas.add_command(label="Sair", command=mensagens_janela)
menu_janela_bloco_notas.add_command(label="Procurar", command=pesquisar_palavra)
menu_janela_bloco_notas.add_command(label="Contador", command=contador)
janela_bloco_notas.config(menu=menu_janela_bloco_notas)


janela_bloco_notas.protocol("WM_DELETE_WINDOW", fechar_janela)
janela_bloco_notas.mainloop()


