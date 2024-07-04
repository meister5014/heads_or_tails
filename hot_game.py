import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"
<<<<<<< HEAD
    
print("Tossing a coin...")
=======

user_name = input("お名前は何ですか？\n> ")
print(f"こんにちは、{user_name}さん！")

print("コインを投げています...")
>>>>>>> user_name
results = [toss_coin() for _ in range(3)]
heads_count = results.count("Heads")
tails_count = results.count("Tails")
    
for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

print(f"Heads: {heads_count}, Tails: {tails_count}")

if head_count > tails_count:
    print(f"{user_name} won!")
else:
    print(f"{user_name} lost.")
