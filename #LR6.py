import json   #зберігання даних у вигляді словників

def add_recipe():
    recipe_name = input("Введіть назву рецепту: ")
    ingredients = input("Введіть інградієнти через кому: ").split(',')
    instructions = input("Введіть інструкцію: ")

    recipe = {
        'name': recipe_name,
        'ingredients': [ingredient.strip() for ingredient in ingredients],
        'instructions': instructions
    }

    with open('recipes.json', 'a') as file: #в режимі дозапису
        file.write(json.dumps(recipe) + '\n') #в рядок

def list_recipes():
    try:
        with open('recipes.json', 'r') as file:
            recipes = [json.loads(line) for line in file] #рядки в словники
        print("\nСписок рецептів:")
        for recipe in recipes:
            print(f" - {recipe['name']}")
    except:
        print("Не знайдено жодного рецепту.")

def search_recipe():
    recipe_name = input("Введіть назву рецепту для пошуку: ")
    try:
        with open('recipes.json', 'r') as file:
            recipes = [json.loads(line) for line in file]
        for recipe in recipes:
            if recipe['name'].lower() == recipe_name.lower():
                print("\nЗнайдено рецепт:")
                print(f"Назва: {recipe['name']}")
                print(f"Інградієнти: {', '.join(recipe['ingredients'])}")
                print(f"Інструкція: {recipe['instructions']}")
                return
        print(f"Не знайдено жодного рецепту з іменем '{recipe_name}'.")
    except:
        print("Такого рецепту не знайдено.")

while True:
    print("\nКнига рецептів")
    print("1. Додати новий рецепт")
    print("2. Показати усі рецепти")
    print("3. Пошук рецепту за іменем")
    print("4. Вийти з програми")

    choice = input("Введіть свій вибір: ")

    if choice == '1':
        add_recipe()
    elif choice == '2':
        list_recipes()
    elif choice == '3':
        search_recipe()
    elif choice == '4':
        print("До побачення!")
        break
    else:
        print("Некоректний вибір. Будь ласка, спробуйте ще раз.")