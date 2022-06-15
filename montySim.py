import random

possible_action = "door 1", "door 2", "door 3"
car_position = random.choice(possible_action)
print(f"car is behind {car_position}")

if car_position == "door 1":
  possible_goat_action = "door 2", "door 3"
  goat_1_position = random.choice(possible_goat_action)
  print(f"goat 1 is behind {goat_1_position}")
  if goat_1_position == "door 2":
    possible_goat2_action = "door 3"
    print(f"goat 2 is bhind {possible_goat2_action}")

if car_position == "door 2":
  possible_goat3_action = "door 1", "door 3"
  goat_1_position2 = random.choice()
