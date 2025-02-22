import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"

user_name = input("Who are you?\n> ")
print(f"Hello, {user_name}!")

print("Tossing a coin...")
results = [toss_coin() for _ in range(3)]
heads_count = results.count("Heads")
tails_count = results.count("Tails")

for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

print(f"Heads: {heads_count}, Tails: {tails_count}")

if heads_count > tails_count:
    print(f"{user_name} won!")
else:
    print(f"{user_name} lost!")
