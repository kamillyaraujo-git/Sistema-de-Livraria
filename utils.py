import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
# criar janela principal de busca
root = tk.Tk()
root.title("Interface de Busca")

# criar o labelFrame para a area de busca

search_frame = tk.LabelFrame(root, text = "Pesquisar")
search_frame.pack(padx = 10, pady = 10)
search_label = Label(search_frame, text = "Digite o termo:")
search_label.pack(side = tk.LEFT, padx = 5, pady = 5)

# campo para entrada de texto (entry)
search_entry = Entry(search_frame)
search_entry.pack(side = tk.LEFT, padx = 5, pady = 5)

# um campo para o botao de busca
search_button = Button(search_frame, text = "Buscar")
search_button.pack(side = tk.LEFT, padx = 5, pady = 5)

# frame info
janela = tk.Tk()
janela.title("Contador e Mensagens")

# cria o frame dentro da janela principal
frame_info = tk.Frame(janela,
bg ="brown",
db = 5,
relief = tk.SUNKEN)

# posiciona o frame na tela
frame_info.pack(padx = 10, pady = 10) # adiciona um espacvamento ao redor do frame

label_info = tk.Label(frame_info, text = "Está é uma área de informações", bg = "brown")
label_info.pack()    

# criar janela principal para a lista

janela = tk.Tk()
janela.title("Frame de Lista")

# criacao do frame
frame_lista = tk.Frame(janela)
frame_lista.pack(pady = 10)

# criar as listas e adicionar itens
frame_lista_livros = tk.Frame(janela, borderwidth = 2, relief = "groove", padx = 10, pady = 10)
frame_lista_livros.pack(pady = 10, padx = 10, fill = "both", expand = True ) # preenche a janela e expande

# adicionar os widgets dentro do frame
titulo_label = tk.Label(frame_lista_livros, text = "Lista de Livros", font =("Arial", 14, "bold") )
titulo_label.pack(pady = 5)

lista_livros_widget = tk.Listbox(frame_lista_livros, text = "Lista de livros", font =("Arial", 14, "bold"))
titulo_label.pack(pady = 5)

lista_livros_widget = tk.Listbox(frame_lista_livros, heigth = 10, width = 40)
lista_livros_widget.pack(pady = 5, fill = "both", expand = True )

# adiciona alguns livros como exemplo 
livros = ["Como eu era antes de voce", "Como perder um homem em 10 dias", "Dom Casmurro" ]
for livro in livros:
     lista_livros_widget.insert(tk.END, livro) # insere o livro no final da lista

# funcao para exibir a messagebox

def messagebox_showinfo():
     
     # definir o titulo a mensagem 
    titulo = "Informação"
    mensagem = "Ação sucedita com susseso!"
    messagebox.showinfo(titulo, mensagem) # metotodo

def messagebox_showerror():
     
     # definir o titulo a mensagem 
     titulo = "ERRO!"
     mensagem = "Ocorreu um erro, tente novamente!"
     messagebox.showinfo(titulo, mensagem) # metodo

def messagebox_showwaming():
     
     # definir o titulo a mansagem
     titulo = "AVISO!"
     mensagem = "Tente novamente mais tarde."
     messagebox.showinfo(titulo, mensagem) # metodo

def messagebox_askyesno():
     
     # definir o titulo a amensagem
     titulo = "CONFIRMAÇÂO"
     mensagem = "Confirmado com susseso!"
     messagebox.showinfo(titulo, mensagem) # metodo