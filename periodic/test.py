import random

elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

def easy():
    points = 0
    try:
        while True:
            print("==================")
            print("Easy mode")
            print("==================")
            number = random.randint(1, 10)
            answer = input(f"Apa nama elemen ke {number} pada periodic table: ")
            element = elements[number - 1]
            if answer.lower() == element.lower():
                print("Jawaban Anda benar!")
                points += 1
            else:
                print(f"Jawaban Anda salah. Elemen yang benar adalah {element}")
                points -= 1
            print(f"Skor Anda saat ini: {points}\n")
    except KeyboardInterrupt:
        print("\nGame selesai! Skor akhir Anda adalah:", points)
    return points

def normal():
    points = 0
    try:
        while True:
            print("==================")
            print("Normal mode")
            print("==================")
            number = random.randint(1, 30)
            answer = input(f"Apa nama elemen ke {number} pada periodic table: ")
            element = elements[number - 1]
            if answer.lower() == element.lower():
                print("Jawaban Anda benar!")
                points += 1
            else:
                print(f"Jawaban Anda salah. Elemen yang benar adalah {element}")
                points -= 1
            print(f"Skor Anda saat ini: {points}\n")
    except KeyboardInterrupt:
        print("\nGame selesai! Skor akhir Anda adalah:", points)
    return points

def hard():
    points = 0
    try:
        while True:
            print("==================")
            print("Hard mode")
            print("==================")
            number = random.randint(1, 80)
            answer = input(f"Apa nama elemen ke {number} pada periodic table: ")
            element = elements[number - 1]
            if answer.lower() == element.lower():
                print("Jawaban Anda benar!")
                points += 1
            else:
                print(f"Jawaban Anda salah. Elemen yang benar adalah {element}")
                points -= 1
            print(f"Skor Anda saat ini: {points}\n")
    except KeyboardInterrupt:
        print("\nGame selesai! Skor akhir Anda adalah:", points)
    return points

def all():
    points = 0
    try:
        while True:
            print("==================")
            print("All mode")
            print("==================")
            number = random.randint(1, 118)
            answer = input(f"Apa nama elemen ke {number} pada periodic table: ")
            element = elements[number - 1]
            if answer.lower() == element.lower():
                print("Jawaban Anda benar!")
                points += 1
            else:
                print(f"Jawaban Anda salah. Elemen yang benar adalah {element}")
                points -= 1
            print(f"Skor Anda saat ini: {points}\n")
    except KeyboardInterrupt:
        print("\nGame selesai! Skor akhir Anda adalah:", points)
    return points
