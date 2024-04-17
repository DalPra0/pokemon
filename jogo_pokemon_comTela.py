import random
import tkinter as tk
from tkinter import Toplevel, ttk

# Dados e lógica do jogo
pokemons_caverna = ['Zubat', 'Geodude', 'Onix', 'Diglett', 'Cubone', 'Sableye', 'Dusclops', 'Regidrago', 'Torkoal']
pokemons_mato = ['Pikachu', 'Rattata', 'Pidgey', 'Bulbasaur', 'Oddish', 'Bellsprout', 'Rellor', 'Togedemaru']
pokedex = []

# Funções
def iniciar_aventura():
    nome = nome_entry.get()
    introducao_label.config(text=f"Olá {nome}, eu sou o Professor Carvalho e vou guiá-lo em sua jornada Pokémon!")
    avancar_button.pack(pady=20)

def avancar():
    aventura_frame.pack()
    bem_vindo_frame.pack_forget()

def explorar(ambiente):
    pokemon = encontrar_pokemon(ambiente)
    if pokemon in pokedex:
        nova_janela = Toplevel(root)
        nova_janela.title("Encontro com Pokémon")
        msg = f"Você encontrou um {pokemon}!\nMas você já capturou este Pokémon antes."
        lbl_msg = tk.Label(nova_janela, text=msg)
        lbl_msg.pack(pady=20)
        btn_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        btn_fechar.pack(pady=10)
    else:
        capturar_pokemon(pokemon, ambiente)


def encontrar_pokemon(ambiente):
    return random.choice(pokemons_caverna if ambiente == 'caverna' else pokemons_mato)

def capturar_pokemon(pokemon, ambiente):
    probabilidade = 50 if ambiente == 'mato' else 35
    
    if 'captura_window' in globals():
        captura_window.destroy()  # Destruir a janela anterior, se existir
    
    captura_window = Toplevel(root)
    captura_window.title("Captura de Pokémon")
    
    if pokemon in pokedex:
        msg = f"Esse Pokémon você já tem!"
        lbl_resultado = tk.Label(captura_window, text=msg)
        lbl_resultado.pack(pady=20)
    else:
        capturado = random.randint(1, 100) <= probabilidade
        if capturado:
            pokedex.append(pokemon)
            msg = f"Parabéns! Você capturou {pokemon}!"
        else:
            msg = f"Ah não! O Pokémon escapou."
            btn_tentar_novamente = tk.Button(captura_window, text="Tentar Capturar Novamente", command=lambda: capturar_pokemon(pokemon, ambiente))
            btn_tentar_novamente.pack(pady=10)
                    
    lbl_resultado = tk.Label(captura_window, text=msg)
    lbl_resultado.pack(pady=20)
    
    btn_fechar = tk.Button(captura_window, text="Fechar", command=captura_window.destroy)
    btn_fechar.pack(side=tk.BOTTOM, pady=10)



def ver_pokedex():
    pokedex_window = Toplevel(root)
    pokedex_window.title("Pokédex")
    if pokedex:
        cols = ('#1', '#2')
        tree = ttk.Treeview(pokedex_window, columns=cols, show='headings')
        tree.heading('#1', text='ID')
        tree.heading('#2', text='Nome')
        for idx, nome in enumerate(pokedex, start=1):
            tree.insert("", "end", values=(idx, nome))
        tree.pack(expand=True, fill='both', padx=10, pady=10)
    else:
        tk.Label(pokedex_window, text="Sua Pokédex está vazia.").pack(pady=20)

# GUI setup
root = tk.Tk()
root.title("Aventura Pokémon")

bem_vindo_frame = tk.Frame(root)
bem_vindo_frame.pack(pady=20)

nome_label = tk.Label(bem_vindo_frame, text="Digite seu nome:")
nome_label.pack()
nome_entry = tk.Entry(bem_vindo_frame)
nome_entry.pack()
iniciar_button = tk.Button(bem_vindo_frame, text="Iniciar Aventura", command=iniciar_aventura)
iniciar_button.pack(pady=10)

introducao_label = tk.Label(bem_vindo_frame, text="")
introducao_label.pack()
avancar_button = tk.Button(bem_vindo_frame, text="Avançar", command=avancar)

aventura_frame = tk.Frame(root)
resultado_label = tk.Label(aventura_frame, text="")
resultado_label.pack()
caverna_button = tk.Button(aventura_frame, text="Explorar Caverna", command=lambda: explorar('caverna'))
caverna_button.pack(side=tk.LEFT)
mato_button = tk.Button(aventura_frame, text="Explorar Mato", command=lambda: explorar('mato'))
mato_button.pack(side=tk.RIGHT)

ver_pokedex_button = tk.Button(aventura_frame, text="Ver Pokédex", command=ver_pokedex)
ver_pokedex_button.pack(side=tk.BOTTOM)  # Adicionando o botão para ver a Pokédex

root.mainloop()
