# -*- coding: utf-8 -*-
from utils import *
"""# 2. <지역, 플레이어, 포켓몬, playerSystem에 대한 객체지향프로그래밍>"""
class Region:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Town(Region):
    def get_region_name(self):
        return 'Town'
    pass
class WildArea(Region):
    def get_region_name(self):
        return 'WildArea'


class Grass(WildArea):
    def get_region_name(self):
        return 'Grass'

class Ground(WildArea):
    def get_region_name(self):
        return 'Ground'

class Dark(WildArea):
    def get_region_name(self):
        return 'Dark'

class Ice(WildArea):
    def get_region_name(self):
        return 'Ice'

class Mountain(WildArea):
    def get_region_name(self):
        return 'Mountain'

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

class Player(Person):
    def __init__(self, name, gender, age, my_pokemon, current_region,determinent):
        super().__init__(name, gender, age)
        self.my_pokemon = my_pokemon
        self.current_region = current_region
        self.determinent = determinent # ai players=> 0, 플레이어 starting pokemon=>1, player 포획 pokemon=>2

    def get_determinent(self):
        return self.determinent
    def set_determinent(self,value):
        self.determinent = value
        return self.determinent


    def move_up(self):
        self.current_region.y += 1
        print('1칸 위로 이동')

    def move_down(self):
        if self.current_region.y >0:
            self.current_region.y -= 1
            print('1칸 아래로 이동')

        else:
            print("더 이상 내려갈 수 없습니다. 그 아래는 절벽입니다.")
            pass

    def move_left(self):
        if self.current_region.x >0:
            self.current_region.x -= 1
            print('1칸 왼쪽으로 이동')

        else:
            print("더 이상 왼쪽으로 갈 수 업습니다. 그 옆은 절벽입니다.")
            pass
    def move_right(self):
        self.current_region.x+=1
        print('1칸 오른쪽으로 이동')

class Pokemon:
    def __init__(self, name, type1, type2, hp,total_hp, attack, defense, speed):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.total_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed


class My_pokemon(Pokemon):
    pass

class Wild_pokemon(Pokemon):
    pass

class PlayerSystem:
    _rankings =[]

    @classmethod
    def register_Player(cls, value):
        cls._rankings.append(value)


    @classmethod
    def rankings(cls):
        return cls._rankings


    @classmethod
    def rank_by_attack(cls,player):
        cls._rankings.sort(key=lambda x: calculate_total_attack(x.my_pokemon)[1], reverse=True)
        info = map(lambda player: f'{cls._rankings.index(player)+1}. 플레이어 이름: {player.name}, 플레이어 공격력: {calculate_total_attack(player.my_pokemon)[1]},\n보유 포켓몬: {calculate_total_pokemon(player.my_pokemon)}\n', cls._rankings)
        result = '\n'.join(info)
        player_rank = cls._rankings.index(player)+1
        print(result)
        print()
        print(f'51명 중 {player.name}의 등수: {player_rank}')

    @classmethod
    def rank_by_defense(cls,player):
        cls._rankings.sort(key=lambda x: calculate_total_defense(x.my_pokemon)[1], reverse=True)
        info = map(lambda player: f'{cls._rankings.index(player)+1}. 플레이어 이름: {player.name}, 플레이어 방어력: {calculate_total_defense(player.my_pokemon)[1]},\n보유 포켓몬: {calculate_total_pokemon(player.my_pokemon)}\n', cls._rankings)
        result = '\n'.join(info)
        player_rank = cls._rankings.index(player)+1
        print(result)
        print()
        print(f'51명 중 {player.name}의 등수: {player_rank}')

    @classmethod
    def rank_by_HP(cls,player):
        cls._rankings.sort(key=lambda x: calculate_total_HP(x.my_pokemon)[1], reverse=True)
        info = map(lambda player: f'{cls._rankings.index(player)+1}. 플레이어 이름: {player.name}, 플레이어 체력: {calculate_total_HP(player.my_pokemon)[1]},\n보유 포켓몬: {calculate_total_pokemon(player.my_pokemon)}\n', cls._rankings)
        result = '\n'.join(info)
        player_rank = cls._rankings.index(player)+1
        print(result)
        print()
        print(f'51명 중 {player.name}의 등수: {player_rank}')


    @classmethod
    def rank_by_speed(cls,player):
        cls._rankings.sort(key=lambda x: calculate_total_speed(x.my_pokemon)[1], reverse=True)
        info = map(lambda player: f'{cls._rankings.index(player)+1}. 플레이어 이름: {player.name}, 플레이어 스피드: {calculate_total_speed(player.my_pokemon)[1]},\n보유 포켓몬: {calculate_total_pokemon(player.my_pokemon)}\n', cls._rankings)
        result = '\n'.join(info)
        player_rank = cls._rankings.index(player)+1
        print(result)
        print()
        print(f'51명 중 {player.name}의 등수: {player_rank}')

