# Given list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]

prime = []
non_prime = []

for num in numbers:
    if num < 2:
        non_prime.append(num)
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                non_prime.append(num)
                break
        else:
            prime.append(num)

print("Prime numbers:", prime)
print("Non-prime numbers:", non_prime)




skills = ['Python', 'Java', 'Python', 'C', 'Java', 'Python', 'HTML', 'C']
skill_count = {}

for skill in skills:
    if skill in skill_count:
        skill_count[skill] += 1
    else:
        skill_count[skill] = 1

print("Skill counts:", skill_count)


