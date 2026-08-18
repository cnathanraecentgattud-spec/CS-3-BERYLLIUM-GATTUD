yearBirth = int(input("Please enter your year of birth: "))

if yearBirth < 1900:
    print("Invalid year, please enter a year not earlier than 1900.")

elif yearBirth > 1900:
    zodiacKey = (yearBirth - 1900) % 12

    zodiacSigns = {
        0: "Rat (鼠 / Shǔ)",
        1: "Ox (牛 / Niú)",
        2: "Tiger (虎 / Hǔ)",
        3: "Rabbit (兔 / Tù)", 
        4: "Dragon (龙 / Lóng)",
        5: "Snake (蛇 / Shé)",
        6: "Horse (马 / Mǎ)",
        7: "Goat (羊 / Yáng)",
        8: "Monkey (猴 / Hóu)",
        9: "Rooster (鸡 / Jī)",
        10: "Dog (狗 / Gǒu)",
        11: "Pig (猪 / Zhū)"
    }

    zodiacSign = zodiacSigns[zodiacKey]
    print(f"Your Chinese zodiac sign is: {zodiacSign}.")
