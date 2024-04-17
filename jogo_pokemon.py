import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

pokemons_caverna = ['Zubat', 'Geodude', 'Onix', 'Diglett', 'Cubone', 'Sableye', 'Dusclops', 'Regidrago', 'Torkoal']
pokemons_mato = ['Pikachu', 'Rattata', 'Pidgey', 'Bulbasaur', 'Oddish', 'Bellsprout', 'Rellor', 'Togedemaru']
pokedex = []
tentativas_extras = 3

def introducao():
    print("Olá, bem-vindo ao mundo Pokémon!")
    nome = input("Por favor, digite seu nome: ")
    print(f"\nOlá {nome}, eu sou o Professor Carvalho e vou guiá-lo em sua jornada Pokémon!")

def explorar_ambiente():
    escolha = input("\nVocê quer entrar na caverna ou explorar o mato? (Digite 'caverna' ou 'mato'): ").lower()
    if escolha != 'caverna' or 'mato':
        print('Essa opção não existe, digite novamente')
        
    return escolha

def encontrar_pokemon(ambiente):
    if ambiente == 'caverna':
        pokemon = random.choice(pokemons_caverna)
    else:
        pokemon = random.choice(pokemons_mato)
    print(f"Você encontrou um {pokemon}!")
    return pokemon

def tentar_novamente(pokemon, ambiente):
    global tentativas_extras
    if tentativas_extras > 0:
        tentar_de_novo = input("Você deseja tentar capturar novamente? (sim/não): ").lower()
        if tentar_de_novo == 'sim':
            tentativas_extras -= 1
            return True
    return False

def capturar_pokemon(pokemon, ambiente):
    global tentativas_extras
    if pokemon in pokedex:
        print(f"Você já tem {pokemon} na sua Pokédex.")
        return
    probabilidade = 50 if ambiente == 'mato' else 35
    capturado = random.randint(1, 100) <= probabilidade

    while not capturado:
        print("Ah não! O Pokémon escapou.")
        if tentar_novamente(pokemon, ambiente):
            capturado = random.randint(1, 100) <= probabilidade
        else:
            return

    pokedex.append(pokemon)
    print(f"Parabéns! Você capturou {pokemon}!")

def listar_pokedex():
    if pokedex:
        print("Pokédex:", pokedex)
    else:
        print("Sua Pokédex está vazia.")

def main():
    introducao()
    while True:
        escolha = explorar_ambiente()
        pokemon_encontrado = encontrar_pokemon(escolha)
        capturar_pokemon(pokemon_encontrado, escolha)
        listar_pokedex()

        continuar = input("Deseja continuar explorando? (sim/não): ").lower()
        if continuar != 'sim':
            print("Obrigado por jogar!")
            break

# Executar o jogo
main()