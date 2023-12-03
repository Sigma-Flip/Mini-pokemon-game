import numpy as np
import matplotlib.pyplot as plt
import re

from battle import *
from env import *
from generate_player import *


def minimap(player):
    with plt.xkcd():
        plt.figure(figsize=(6, 3))

        plt.fill_between(range(5, 11), 0, 10, color='lightgray')
        plt.text(7.5, 5, 'Mountain', color='black', fontsize=10, ha='center', va='center')

        plt.fill_between(range(5, 11), 10, 20, color='blue')
        plt.text(7.5, 15, 'Ice', color='black', fontsize=10, ha='center', va='center')

        plt.fill_between(range(0, 6), 20, 30, color='brown')
        plt.text(2.5, 25, 'Ground', color='black', fontsize=10, ha='center', va='center')

        plt.fill_between(range(5, 11), 20, 30, color='lightgreen')
        plt.text(7.5, 25, 'Grass', color='black', fontsize=10, ha='center', va='center')

        plt.fill_between(range(0, 6), 0, 10, color='skyblue')
        plt.text(2.5, 5, 'Town', color='black', fontsize=10, ha='center', va='center')

        plt.scatter(player.current_region.x, player.current_region.y,s=100 ,color='magenta', marker='X')

        plt.xlim(0, 10)
        plt.ylim(0, 30)

        plt.show()
def pokemon_dictionary(player, df):
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    starting = player.my_pokemon[0:3]
    captured = player.my_pokemon[3:]

    # 내 포켓몬 정보 출력
    starting.sort(key=lambda x: x.__dict__['attack'], reverse=True)
    for i, pokemon in enumerate(starting):
        print(f"----------스타팅 포켓몬 정보 {i+1}----------")
        print(f"이름: {pokemon.name} 타입1: {pokemon.type1} 타입2: {pokemon.type2} 체력: {pokemon.total_hp} 공격: {pokemon.attack} 방어: {pokemon.defense} 스피드: {pokemon.speed}")
        print()


    captured.sort(key=lambda x: x.__dict__['attack'], reverse=True)
    for i, pokemon in enumerate(captured):
        print(f"----------포획한 포켓몬 정보 {i+1}----------")
        print(f"이름: {pokemon.name} 타입1: {pokemon.type1} 타입2: {pokemon.type2} 체력: {pokemon.total_hp} 공격: {pokemon.attack} 방어: {pokemon.defense} 스피드: {pokemon.speed}")
        print()





    while True:
        # 자세히 보고 싶은 포켓몬 선택

        try:
            index = int(input("자세히 보고 싶은 포켓몬의 번호를 입력해주세요 (숫자만): ")) - 1
            selected_pokemon = player.my_pokemon[index]

        except (IndexError, ValueError):
            print("유효한 번호를 입력해 주세요!")
            continue



        selected_pokemon = player.my_pokemon[index]


        # 전체 포켓몬과의 체력 비교
        fig, ax = plt.subplots(figsize=(4, 3))

        sns.histplot(data=df, x="HP", color="blue", alpha=0.5, label="every pokemon")
        plt.axvline(selected_pokemon.total_hp, color = 'red', linestyle='-', label = selected_pokemon.name)

        ax.set_title("HP Distribution ")
        ax.legend()

        plt.show()

         # 전체 포켓몬과의 공격력 비교
        fig, ax = plt.subplots(figsize=(4, 3))

        sns.histplot(data=df, x="Attack", color="blue", alpha=0.5, label="every pokemon")
        plt.axvline(selected_pokemon.attack, color = 'red', linestyle='-',label = selected_pokemon.name)

        ax.set_title("Attack Distribution")
        ax.legend()

        plt.show()

         # 전체 포켓몬과의 방어력 비교
        fig, ax = plt.subplots(figsize=(4, 3))

        sns.histplot(data=df, x="Defense", color="blue", alpha=0.5, label="every pokemon")
        plt.axvline(selected_pokemon.defense, color = 'red', linestyle='-',label = selected_pokemon.name)

        ax.set_title("Defense Distribution")
        ax.legend()

        plt.show()

         # 전체 포켓몬과의 스피드 비교
        fig, ax = plt.subplots(figsize=(4, 3))

        sns.histplot(data=df, x="Speed", color="blue", alpha=0.5, label="every pokemon")
        plt.axvline(selected_pokemon.speed, color = 'red', linestyle='-',label = selected_pokemon.name)

        ax.set_title("Speed Distribution ")
        ax.legend()

        plt.show()


        quit = input("나가려면 0을 입력해주세요 : (계속 보고싶으면 아무 키나) ")
        if quit =="0":
            break

"""# 8. <부가기능> - 도감 출력(FILE I/O)"""
def save_pokemon_dictionary(player, df):
    filename = 'pokemon_dictionary.txt'
    with open(filename, 'w') as file:
        file.write("플레이어 정보\n")
        file.write(f"이름: {player.name}\n")
        file.write(f"성별: {player.gender}\n")
        file.write(f"나이: {player.age}\n")
        file.write("\n")
        file.write("포켓몬 도감\n")
        for pokemon in player.my_pokemon:
            file.write(f"이름: {pokemon.name}\n")
            file.write(f"타입1: {pokemon.type1}\n")
            file.write(f"타입2: {pokemon.type2}\n")
            file.write(f"체력: {pokemon.hp}\n")
            file.write(f"공격력: {pokemon.attack}\n")
            file.write(f"방어력: {pokemon.defense}\n")
            file.write("\n")

    print("포켓몬 도감을 파일에 저장했습니다. 파일 이름 : pokemon_dictionary.txt")

"""# 9. <부가기능> - 정규식 활용한 포켓몬 검색"""
def search_pokemon_by_name(pattern, df, search_direction):
    if search_direction == 1:
        r = re.compile(f"^{pattern}", re.I)
        search_type = "전방"
    elif search_direction == 2:
        r = re.compile(f"{pattern}$", re.I)
        search_type = "후방"
    else:
        raise ValueError("잘못된 검색 방향입니다. 1 또는 2를 입력하세요.")

    matching_pokemon = df[df['Name'].str.findall(r).apply(lambda x: len(x) > 0)]

    if len(matching_pokemon) == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"{search_type} 검색 결과:")
        print(matching_pokemon)

    return matching_pokemon


def calculate_total_pokemon(player_pokemons):
    name_array = np.array([pokemon.name for pokemon in player_pokemons],dtype=object)
    return name_array

def calculate_total_attack(player_pokemons):
    attack_array = np.array([pokemon.attack for pokemon in player_pokemons])
    total_attack = np.sum(attack_array)
    return [attack_array, total_attack]

def calculate_total_defense(player_pokemons):
    defense_array = np.array([pokemon.defense for pokemon in player_pokemons])
    total_defense = np.sum(defense_array)
    return [defense_array, total_defense]

def calculate_total_HP(player_pokemons):
    HP_array = np.array([pokemon.total_hp for pokemon in player_pokemons])
    total_HP = np.sum(HP_array)
    return [HP_array, total_HP]

def calculate_total_speed(player_pokemons):
    speed_array = np.array([pokemon.speed for pokemon in player_pokemons])
    total_speed = np.sum(speed_array)
    return [speed_array, total_speed]

def randomplayers(df_player,df):
    name_list, gender_list = playerDB(df_player)
    for i in pick_randomPlayer(name_list, gender_list,df):
        name = name_list[i]
        gender = gender_list[i]
        computer = randomPlayerGenerator(name,gender,df)
        PlayerSystem.register_Player(computer)

