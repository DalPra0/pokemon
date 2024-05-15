import random

pokemons_caverna = ['Zubat', 'Geodude', 'Onix', 'Diglett', 'Cubone', 'Sableye', 'Dusclops', 'Regidrago', 'Torkoal']
pokemons_mato = ['Pikachu', 'Rattata', 'Pidgey', 'Oddish', 'Bellsprout', 'Rellor', 'Togedemaru']
pokemons_iniciais = ['Bulbasaur', 'Squirtle', 'Charmander']
pokedex = []
tentativas_extras = 3

def introducao():
    print("Olá, bem-vindo ao mundo Pokémon!")
    nome = input("Por favor, digite seu nome: ")
    print(f"\nOlá {nome}, eu sou o Professor Carvalho e vou guiá-lo em sua jornada Pokémon!")

def escolhapokemon_inicial():
    print("\nEscolha o seu Pokémon:")
    print("1. Escolher um Pokémon inicial")
    print("2. Escolher um Pokémon aleatório")
    escolha = input("Digite o número correspondente à sua escolha: ")
    if escolha == '1':
        print("\nEscolha o seu Pokémon inicial:")
        for i, pokemon in enumerate(pokemons_iniciais):
            print(f"{i + 1}. {pokemon}")
        escolha_index = int(input("Digite o número correspondente ao Pokémon que você deseja escolher: ")) - 1
        pokemon_escolhido = pokemons_iniciais[escolha_index]
    elif escolha == '2':
        pokemon_escolhido = random.choice(pokemons_iniciais + pokemons_caverna + pokemons_mato)
        print(f"\nVocê escolheu um Pokémon aleatório e recebeu: {pokemon_escolhido}!")
    else:
        print("Escolha inválida. Por favor, tente novamente.")
        return escolhapokemon_inicial()
    pokedex.append(f"{pokemon_escolhido}*")

def calcular_pokebolas_achadas():
    return random.randint(0, 2)

def explorar_ambiente():
    escolha = input("\nVocê quer entrar na caverna ou explorar o mato? (Digite 'caverna' ou 'mato'): ").lower()
    if escolha != 'caverna' and escolha != 'mato':
        print('Essa opção não existe, digite novamente')
        return explorar_ambiente()
    pokebolas_encontradas = calcular_pokebolas_achadas()
    print(f"Você encontrou {pokebolas_encontradas} Pokébola(s)!")
    global tentativas_extras
    tentativas_extras += pokebolas_encontradas
    return escolha

def encontrar_pokemon(ambiente):
    if ambiente == 'caverna':
        pokemon = random.choice(pokemons_caverna)
    elif ambiente == 'mato':
        pokemon = random.choice(pokemons_mato)
    else:
        return
    print(f"Você encontrou um {pokemon}!")
    opt = input("Deseja capturar? (sim/não): ")
    if opt == 'sim':
        return pokemon
    elif opt == 'não':
        return explorar_ambiente()
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
    elif pokemon in pokemons_iniciais:
        print(f"Você não pode capturar o mesmo Pokémon inicial novamente.")
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
    escolhapokemon_inicial()
    while True:
        escolha = explorar_ambiente()
        pokemon_encontrado = encontrar_pokemon(escolha)
        capturar_pokemon(pokemon_encontrado, escolha)
        listar_pokedex()

        continuar = input("Deseja continuar explorando? (sim/não): ").lower()
        if continuar != 'sim':
            print("Obrigado por jogar!")
            break

main()
