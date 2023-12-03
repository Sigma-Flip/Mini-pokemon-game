import numpy as np
import random

from battle import *
from env import *
from utils import *
from generate_pokemon import *



"""# 5. <플레이어 생성 및 지역이동에 관한 코드>"""

def player_info():
    while True:
        try:
            name = input("이름을 입력하시오: ")
            if not name:
                raise ValueError("이름은 반드시 입력해야 합니다.")
            break
        except ValueError as e:
            print(f"올바른 형식의 이름을 입력해주세요. 오류 메시지: {str(e)}")

    while True:
        try:
            gender = input("성별을 입력하시오: (남 or 여)")
            if gender != "남" and gender != "여":
                raise ValueError("성별은 '남' 또는 '여'로 입력해야 합니다.")
            break
        except ValueError as e:
            print(f"올바른 형식의 성별을 입력해주세요. 오류 메시지: {str(e)}")

    while True:
        try:
            age = input("나이를 입력하시오 : (숫자만)")
            if not age.isdigit():
                raise ValueError("나이는 숫자로만 입력해야 합니다.")
            break
        except ValueError as e:
            print(f"올바른 형식의 나이를 입력해주세요. 오류 메시지: {str(e)}")
    return (name, gender, age)

def DFclassifier(player, df_grass, df_ground, df_ice, df_mountain, df_dark):
    if player.current_region.get_region_name()=='Town':
        return []
    elif player.current_region.get_region_name()=='Grass':
        return df_grass
    elif player.current_region.get_region_name()=='Ground':
        return df_ground
    elif player.current_region.get_region_name()=='Ice':
        return df_ice
    elif player.current_region.get_region_name()=='Mountain':
        return df_mountain
    elif player.current_region.get_region_name()=='Dark':
        return df_dark
    else:
        print("정의되지 않은 지역임")

def change_region(player, current_x, current_y):
    if current_x >= 0 and current_x <= 5 and current_y >= 0 and current_y <= 10:
        player.current_region = Town(current_x, current_y)
        print("---------------------------------------------")
        print("마을에 도착했습니다. 포켓몬이 등장하지 않는 안전구역입니다!")
        print("---------------------------------------------")

    elif current_x >= 5 and current_x <= 10 and current_y >= 0 and current_y <= 10:
        player.current_region = Mountain(current_x, current_y)
        print("---------------------------------------------")
        print("산에 도착했습니다. Mountain 타입의 포켓몬들이 등장합니다!")
        print("---------------------------------------------")

    elif current_x >= 5 and current_x <= 10 and current_y >= 10 and current_y <= 20:
        player.current_region = Ice(current_x, current_y)
        print("---------------------------------------------")
        print("빙하에 도착했습니다. Ice 타입의 포켓몬들이 등장합니다!")
        print("---------------------------------------------")
    elif current_x >= 0 and current_x <= 5 and current_y >= 20 and current_y <= 30:
        player.current_region = Ground(current_x, current_y)
        print("---------------------------------------------")
        print("메마른 땅에 도착했습니다. Ground 타입의 포켓몬들이 등장합니다!")
        print("---------------------------------------------")
    elif current_x >= 5 and current_x <= 10 and current_y >= 20 and current_y <= 30:
        player.current_region = Grass(current_x, current_y)
        print("---------------------------------------------")
        print("초원에 도착했습니다. Grass 타입의 포켓몬들이 등장합니다!")
        print("---------------------------------------------")
    else:
        player.current_region = Dark(current_x, current_y)
        print("---------------------------------------------")
        print("이제부터는 암흑세계입니다. Dark와 Ghost 타입의 포켓몬들이 등장합니다!")
        print("---------------------------------------------")

def playerDB(df_player):
    # 정규식 패턴
    pattern = r'^(.*?),(.*?),(.*?)$'

    # 정규식을 적용하여 열 분할
    df_player[['name', 'gender', 'count']] = df_player['Name'].str.extract(pattern)

    # 'Name' 열 제거
    df_player = df_player.drop('Name', axis=1)

    df_player['gender'] = df_player['gender'].map({'M': '남성', 'F': '여성'})

    return [ df_player['name'], df_player['gender']]

def pick_randomPlayer(name, gender,df):

    sample_size=50
    random_index = random.sample(range(len(name)+1), sample_size)


    return random_index

def randomPlayerGenerator(name, gender,df):
    age =np.random.randint(15,65) # 생산가능인구 가정
    start_pokemon=[]
    start_region= Town(0,0)
    player = Player(name, gender ,age, start_pokemon, start_region,0)
    for i in range(3):
        pokemon = create_random_pokemon(df)
        player.my_pokemon.append(pokemon)
    return player