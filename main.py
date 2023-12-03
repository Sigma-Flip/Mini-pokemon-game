
from utils import *


if __name__ == "__main__":
    ### 파일 위치
    file_path_pokemon = './pokemon_db_1.csv'
    file_path_player_info = './yob_2022.csv'
    df = pd.read_csv(file_path_pokemon, encoding='euc-kr')
    df = df.drop(columns=['Sp. Atk', 'Sp. Def', 'Generation', 'Legendary', '#'], axis=1)
    df_player = pd.read_csv(file_path_player_info, encoding='euc-kr')
    df_player.index.name = 'Name'

    # 지역 별 dataframe 생성

    df_grass = df[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Grass')]
    df_ground = df[(df['Type 1'] == 'Ground') | (df['Type 2'] == 'Ground')]
    df_dark = df[
        (df['Type 1'] == 'Dark') | (df['Type 2'] == 'Dark') | (df['Type 1'] == 'Ghost') | (df['Type 2'] == 'Ghost')]
    df_ice = df[(df['Type 1'] == 'Ice') | (df['Type 2'] == 'Ice')]
    df_mountain = df[(df['Type 1'] == 'Mountain') | (df['Type 2'] == 'Mountain')]


    # 플레이어 정보 입력
    start_pokemon = []
    start_region = Town(0, 0)
    name, gender, age = player_info()
    print("플레이어 정보입력이 완성되었습니다!!")
    print("---------------------------")
    print()

    player = Player(name, gender, age, start_pokemon, start_region,1)
    PlayerSystem.register_Player(player)
    startingpokemon(player, df)
    randomplayers(df_player= df_player, df= df)
    ###### 게임 시작 #######
    print("***Welcome to Pokemon World***")
    print()
    print("당신의 이름은 ",player.name,"입니다!")
    print("-------------------------------------------플레이어 정보-------------------------------------------")
    print(f'성별 : {player.gender}, 나이: {player.age}, 현재위치: x={player.current_region.x} y={player.current_region.y}')
    print(f'-------------------------------------------보유 포켓몬---------------------------------------------')
    for i in player.my_pokemon:
        print(i.name)
    print()


    while True:
        print(f'현재 위치 :  {player.current_region.get_region_name()}({player.current_region.x}, {player.current_region.y})')
        action = input("무엇을 할까요? 1. move up 2. move down 3. move left 4. move right 5. 포켓몬 도감 6. 미니맵 7. 도감 저장 8. 검색 9.다른 플레이어들 10. 종료")
        print()
        wild_pokemon = create_random_pokemon(DFclassifier(player, df_grass=df_grass, df_ground=df_ground, df_ice=df_ice, df_dark=df_dark, df_mountain=df_mountain))
        if action=="1":
            player.move_up()
            change_region(player,player.current_region.x, player.current_region.y)
            encounter_wildpokemon(player, wild_pokemon)

        elif action=="2":
            player.move_down()
            change_region(player,player.current_region.x, player.current_region.y)
            encounter_wildpokemon(player, wild_pokemon)

        elif action=="3":
            player.move_left()
            change_region(player, player.current_region.x, player.current_region.y)
            encounter_wildpokemon(player, wild_pokemon)


        elif action=="4":
            player.move_right()
            change_region(player, player.current_region.x, player.current_region.y)
            encounter_wildpokemon(player, wild_pokemon)

        elif action=="5":
            pokemon_dictionary(player, df)

        elif action=="6":
            minimap(player)

        elif action=="7":
            save_pokemon_dictionary(player, df)

        elif action=="8":
            while True:
                try:
                    print('''
                    **********검색기 사용법***************
                    1. 전방검색 : 찾고자 하는 포켓몬의 처음 이름과 매치됩니다.(ex. input:[pi] result:[pichu],,, )
                    2. 후방검색 : 찾고자 하는 포켓몬의 마지막 이름과 매치됩니다. (ex. input:[chu] result:[pichu],,,)
                    3. 대소문자의 구별없이 검색합니다.
                    **********************************
                    ''')
                    search_direction = int(input("1: 전방검색 2: 후방검색. 숫자를 입력해주세요."))
                    if search_direction != 1 and search_direction != 2:
                        raise ValueError
                    pattern = input("찾고싶은 포켓몬의 알파벳을 적어주세요: (나가려면 'quit'을 입력하세요)")
                    if pattern =='quit':
                        break

                    search_pokemon_by_name(pattern, df,search_direction)
                except ValueError:
                    print("다시 해주세요")
                    continue

        elif action=="9":
            response = int(input('1. 공격력순 2. 방어력순 3. HP순 4. 스피드순'))
            print()
            if response==1:
                PlayerSystem.rank_by_attack(player)
            elif response==2:
                PlayerSystem.rank_by_defense(player)
            elif response==3:
                PlayerSystem.rank_by_HP(player)
            elif response==4:
                PlayerSystem.rank_by_speed(player)
            else:
                print('올바른 숫자를 입력해주세요')
                continue

        elif action=="10":
            response = input(f'정말로 게임을 종료하시겠습니까? Y/N')
            if response =='Y':
                print("게임을 종료합니다...")
                break
            elif response =="N":
                pass
            else:
                print("Y/N 중에 눌러주세요")

        else:
            print("올바른 입력을 해주세요")
            continue


