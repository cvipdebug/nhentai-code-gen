import requests, random, string, gratient
from os import system

system('cls && title Nhentai Code Gen By Cvip')

title_stuff = []
working = 0
nun = 0
all = 0

numbers = [
    1,
    2,
    3,
    4,
    5,
    6
]

while True:
    nunn = random.choice(numbers)
    gen = ('').join(random.choice(string.digits)for k in range(nunn))
    link = f'https://nhentai.net/g/{gen}/'
    r = requests.get(link)
    if r.status_code == 200:
        all += 1
        working += 1
        system('title Working : ' + str(working) + ' All : ' + str(all) + ' Not Working : ' + str(nun) + " Made By Cvip")
        print(gratient.green(f"Working link : {link}"))
        file = open("codes.txt", "a")
        file.write(f"{link}\n")
        file.close()
    else:
        all += 1
        nun += 1
        system('title Working : ' + str(working) + ' All : ' + str(all) + ' Not Working : ' + str(nun) + " Made By Cvip")
        print(gratient.red(f"Not Working : {link}"))