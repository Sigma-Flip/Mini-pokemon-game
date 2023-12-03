import numpy as np
from battle import *
from env import *



"""# 4. < 랜덤 포켓몬 생성 및 야생포켓몬 관련 코드>"""

def create_random_pokemon(df):
    if len(df)<=0:
        pass
    else:
        index = np.random.randint(0,len(df)-1)
        pokemon_info = df.iloc[index]
        name = pokemon_info['Name']
        type1 = pokemon_info['Type 1']
        type2 = pokemon_info['Type 2']
        total_hp = pokemon_info['HP']
        hp = pokemon_info['HP']
        attack = pokemon_info['Attack']
        defense = pokemon_info['Defense']
        speed = pokemon_info['Speed']

        pokemon = Pokemon(name, type1, type2, hp,total_hp, attack, defense, speed)
        return pokemon

def startingpokemon(player,df):
    count=0
    while True:
        print()
        print()
        print("랜덤으로 스타팅 포켓몬이 정해집니다.")
        print("총 3마리를 고를 수 있으며, 원하지 않으면 다른 포켓몬을 뽑을 수도 있습니다!")
        print()
        random_pokemon = create_random_pokemon(df)
        print(f'축하드립니다! 랜덤 포켓몬 : {random_pokemon.name}')
        print(f'--------------정보---------------')
        print(f'타입 : {random_pokemon.type1}, {random_pokemon.type2} 공격력: {random_pokemon.attack}, 수비력: {random_pokemon.defense}, 스피드 : {random_pokemon.speed},  체력: {random_pokemon.total_hp}')
        accept = input(f"{random_pokemon.name}으로 정하시겠습니까? 예/아니요: ")

        if accept=="예":
            count+=1
            my_pokemon1=My_pokemon(random_pokemon.name,random_pokemon.type1,random_pokemon.type2, random_pokemon.hp, random_pokemon.total_hp, random_pokemon.attack, random_pokemon.defense, random_pokemon.speed)

            player.my_pokemon.append(my_pokemon1)

        elif accept =="아니요":
            print("아쉽군요. 다시 포켓몬을 뽑겠습니다!")
            print()
            pass
        else:
            print("잘못된 입력입니다.다시 입력해주세요. 다시 포켓몬을 뽑겠습니다!")
            print()
            continue

        if count==3:
            print()
            print("스타팅 포켓몬 선정이 완료되었습니다. 게임을 시작합니다!")
            print("...")
            print("...")
            print()
            print()

            break

def encounter_wildpokemon(player, wild_pokemon):
    try:
        prob = np.random.randint(0,10)
        if prob <=3: # 낮은 확률로 야생 포켓몬 만남
            if len(player.my_pokemon) > 0:
                print(f"야생의 {wild_pokemon.name}이 등장했습니다!")
                battle(player, wild_pokemon)
            else:
                print("You don't have any Pokemon to battle!")
    except:
        pass

