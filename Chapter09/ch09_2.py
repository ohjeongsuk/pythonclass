# 상속

# 일반유닛
class Unit:
  # 생성자
  def  __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    # print(f"유닛이름: {self.name} 체력:{self.hp} 이동속도:{self.speed} 생성완료")
  def move(self, location):
    print(f"[지상 유닛 이동]")
    print(f"{self.name}유닛이 체력:{self.hp}, {location}시 방향으로 이동중")

class AttackUnit(Unit):
  # 생성자
  def __init__(self, name, hp, ad, speed):
    # 부모생성자 책임을 진다.
    Unit.__init__(self, name, hp, speed)
    self.ad = ad
    print(f"{self.name} 유닛이 체력:{self.hp}, 공격력:{self.ad}, 이동속도:{self.speed} 유닛이 생성됨")


  # 멤버함수(공격함수)
  def attack(self, location):
    print(f"{self.name}가 {location}시 방향으로 공격력{self.ad}으로 공격하고 있습니다.")

  # 멤버함수(공격을 당하는함수)
  def damaged(self, ad):
    print(f"{self.name}가 상대방으로 부터 공격력{ad}으로 공격받고 있습니다.")
    self.hp = self.hp - ad
    print(f"{self.name}가 공격을 받아서 남은 체력{self.hp}입니다.")
    if self.hp <= 0:
      print(f"{self.name}유닛은 파괴되었습니다.")

  # 오버라이딩
  def move(self, location):
    print(f"[지상 자식 유닛 이동]")
    print(f"{self.name}유닛이 체력:{self.hp} 공격력:{self.ad} , {location}시 방향으로 이동중")

# 보병, 탱크 유닛 생성
soldier1 = AttackUnit("보병1", 40, 5, 10)
soldier2 = AttackUnit("보병2", 40, 5, 10)
soldier3 = AttackUnit("보병3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 130, 35, 20)
tank2 = AttackUnit("탱크2", 130, 35, 20)

# 배열관리 공격지시
attack_list = []
attack_list.append(soldier1)
attack_list.append(soldier2)
attack_list.append(soldier3)
attack_list.append(tank1)
attack_list.append(tank2)

for unit in attack_list:
  # unit.attack(2)
  unit.move(10)

# for unit in attack_list: 
#   unit.damaged(10)

# 상속(오버라이딩과 다형성구현이 가장 중요한 개념)