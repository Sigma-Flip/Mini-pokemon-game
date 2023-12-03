import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
import datetime

def checkTime(func):

    def new_func(*args, **kwargs):
        start = time.time()
        now = datetime.datetime.now()
        dt = now.strftime("[%Y-%m-%d %H:%M]")
        print(dt)

        func(*args, **kwargs)
        end = time.time()

        playtime = end-start

        print()
        print("전투가 ",playtime,'초 걸렸습니다!')


    return new_func

def remaining_health(pokemon):
    if pokemon.hp > 0:
        df_health = pd.DataFrame({'HP': [pokemon.hp], 'Damage': [pokemon.total_hp - pokemon.hp]}, index=[pokemon.name])
    elif pokemon.hp <= 0:
        df_health = pd.DataFrame({'HP': 0, 'Damage': [pokemon.total_hp]}, index=[pokemon.name])


    df_health.plot(kind='barh',figsize=(7,2), stacked=True, alpha=0.7,color=['red','grey'], )
    plt.xlabel('HP')
    plt.ylabel('Pokemon')
    plt.title('Pokemon Health')
    plt.legend()
    plt.show()

@checkTime
def battle(player, wild_pokemon):


    for i,pokemon in enumerate(player.my_pokemon):
        print(f'{i+1}. {pokemon.name}')
    while True:
        try:
            index = int(input("포켓몬을 골라주십시오(숫자)"))-1
            my_battle_pokemon = player.my_pokemon[index]
            print(f'{my_battle_pokemon.name}! 가라!')
            break
        except (IndexError, ValueError):
            print("범위 안의 번호를 입력해주세요!")
            continue


    if my_battle_pokemon.speed > wild_pokemon.speed:
        print(f'우리의 {my_battle_pokemon.name}의 스피드가 더욱 빨라 {my_battle_pokemon.name} 이/가 먼저 공격합니다!')
    else:
        print(f'야생의 {wild_pokemon.name}의 스피드가 더욱 빨라 {wild_pokemon.name} 이/가 먼저 공격합니다')

    while True:
        action = input("무엇을 하시겠습니까? 1.배틀 2.포획 3.도망 : ")
        print()

        #battle
        if action=='1':

            if my_battle_pokemon.speed >= wild_pokemon.speed:
                print("플레이어의 턴입니다")
                if my_battle_pokemon.attack > wild_pokemon.defense:
                    damage = my_battle_pokemon.attack - wild_pokemon.defense
                    wild_pokemon.hp -= damage
                    print(f'야생의 {wild_pokemon.name} 이/가 {damage}만큼 피해를 입었습니다!')
                    print(f'야생의 {wild_pokemon.name} 의 남은 체력 : {wild_pokemon.hp}')
                    print()
                    remaining_health(wild_pokemon)

                    if wild_pokemon.hp <=0:
                        print(f'야생의 {wild_pokemon.name}이/가 쓰러졌습니다!')
                        wild_pokemon.hp = wild_pokemon.total_hp
                        print("배틀을 종료합니다!")
                        break

                else:
                    print(f'야생의 {wild_pokemon.name}의 방어력이 너무 높아 피해를 입지 않았습니다 도망이 답입니다')


                print("상대방의 턴입니다.")
                if my_battle_pokemon.defense < wild_pokemon.attack:
                    damage = wild_pokemon.attack - my_battle_pokemon.defense
                    my_battle_pokemon.hp -= damage
                    print(f'우리의 {my_battle_pokemon.name} 이/가 {damage}만큼 피해를 입었습니다!')
                    print(f'우리의 {my_battle_pokemon.name} 의 남은 체력 : {my_battle_pokemon.hp}')
                    print()
                    remaining_health(my_battle_pokemon)

                    if my_battle_pokemon.hp <=0:
                        print(f'우리의 {my_battle_pokemon.name}이/가 쓰러졌습니다!')
                        print("배틀을 종료합니다!")
                        my_battle_pokemon.hp = my_battle_pokemon.total_hp
                        break
                else:
                    print(f'우리의 {my_battle_pokemon.name}의 방어력이 너무 높아 피해를 입지 않았습니다')



            # 상대방의 스피드가 더 빠를 경우
            else:

                print("상대방의 턴입니다.")
                if my_battle_pokemon.defense < wild_pokemon.attack:
                    damage = wild_pokemon.attack - my_battle_pokemon.defense
                    my_battle_pokemon.hp -= damage
                    print(f'우리의 {my_battle_pokemon.name} 이/가 {damage}만큼 피해를 입었습니다!')
                    print(f'우리의 {my_battle_pokemon.name} 의 남은 체력 : {my_battle_pokemon.hp}')
                    print()
                    remaining_health(my_battle_pokemon)

                    if my_battle_pokemon.hp <=0:
                        print(f'우리의 {my_battle_pokemon.name}이/가 쓰러졌습니다!')
                        print("배틀을 종료합니다!")
                        print()
                        my_battle_pokemon.hp = my_battle_pokemon.total_hp
                        break
                else:
                    print(f'우리의 {my_battle_pokemon.name}의 방어력이 너무 높아 피해를 입지 않았습니다')
                    print()

                print("플레이어의 턴입니다")
                if my_battle_pokemon.attack > wild_pokemon.defense:
                    damage = my_battle_pokemon.attack - wild_pokemon.defense
                    wild_pokemon.hp -= damage
                    print(f'야생의 {wild_pokemon.name} 이/가 {damage}만큼 피해를 입었습니다!')
                    print(f'야생의 {wild_pokemon.name} 의 남은 체력 : {wild_pokemon.hp}')
                    print()
                    remaining_health(wild_pokemon)

                    if wild_pokemon.hp <=0:
                        print(f'야생의 {wild_pokemon.name}이/가 쓰러졌습니다!')
                        print("배틀을 종료합니다!")
                        print()
                        wild_pokemon.hp = wild_pokemon.total_hp
                        break
                else:
                    print(f'야생의{wild_pokemon.name}의 방어력이 너무 높아 피해를 입지 않았습니다 도망이 답입니다')
                    print()


        elif action=='2':
            prob = random.random()
            capture_prob = 1-(wild_pokemon.hp/wild_pokemon.total_hp)

            if capture_prob >= prob:
                print("포획에 성공하였습니다!")
                wild_pokemon.hp = wild_pokemon.total_hp
                player.my_pokemon.append(wild_pokemon)
                print("배틀을 종료합니다")
                print()
                break
            else:
                print("포획에 실패했습니다!")
                print()

        elif action=='3':
            print("성공적으로 도망쳤습니다!")
            break