# # importing necessary libraries/modules
# import nltk
import random
# from nltk.corpus import words

# nltk.download('words')



# word_list = words.words()
# print(word_list)









# using manual lists:-

# word_list imported from chatGPT

words = [
    'apple', 'banana', 'grape', 'orange', 'peach', 'berry', 'melon', 'kiwi', 'pear', 'plum',
    'mango', 'cherry', 'lemon', 'lime', 'fig', 'date', 'olive', 'apricot', 'guava', 'papaya',
    'tomato', 'onion', 'garlic', 'ginger', 'pepper', 'carrot', 'cabbage', 'potato', 'radish', 'bean',
    'beet', 'pea', 'spinach', 'lettuce', 'broccoli', 'zucchini', 'cauliflower', 'celery', 'okra', 'corn',
    'oat', 'rice', 'wheat', 'barley', 'rye', 'buckwheat', 'quinoa', 'millet', 'flour', 'grain',
    'milk', 'butter', 'cheese', 'yogurt', 'cream', 'bread', 'toast', 'sandwich', 'bagel', 'muffin',
    'cake', 'cookie', 'brownie', 'pie', 'donut', 'tart', 'biscuit', 'pancake', 'waffle', 'crumpet',
    'egg', 'bacon', 'ham', 'sausage', 'steak', 'chicken', 'beef', 'pork', 'fish', 'shrimp',
    'lobster', 'crab', 'clam', 'oyster', 'squid', 'octopus', 'tuna', 'salmon', 'trout', 'cod',
    'spaghetti', 'macaroni', 'noodle', 'lasagna', 'pizza', 'burger', 'hotdog', 'fries', 'ketchup', 'mustard',
    'salad', 'soup', 'stew', 'curry', 'salsa', 'chili', 'gravy', 'sauce', 'dip', 'spread',
    'jam', 'jelly', 'honey', 'syrup', 'butter', 'mayo', 'oil', 'vinegar', 'salt', 'pepper',
    'sugar', 'spice', 'herb', 'basil', 'parsley', 'thyme', 'rosemary', 'cumin', 'cinnamon', 'ginger',
    'cardamom', 'clove', 'nutmeg', 'saffron', 'paprika', 'turmeric', 'oregano', 'dill', 'mint', 'vanilla',
    'water', 'juice', 'soda', 'tea', 'coffee', 'milkshake', 'smoothie', 'lemonade', 'wine', 'beer',
    'whiskey', 'vodka', 'rum', 'gin', 'brandy', 'champagne', 'cider', 'milk', 'cocoa', 'latte',
    'book', 'pen', 'pencil', 'paper', 'eraser', 'ruler', 'marker', 'crayon', 'chalk', 'glue',
    'scissors', 'tape', 'stapler', 'clip', 'notebook', 'folder', 'binder', 'desk', 'chair', 'lamp',
    'computer', 'laptop', 'tablet', 'phone', 'camera', 'printer', 'mouse', 'keyboard', 'monitor', 'screen',
    'speaker', 'headphone', 'microphone', 'remote', 'charger', 'cable', 'battery', 'clock', 'watch', 'calendar',
    'shoe', 'sock', 'shirt', 'pants', 'shorts', 'jacket', 'coat', 'hat', 'scarf', 'glove',
    'belt', 'tie', 'dress', 'skirt', 'blouse', 'sweater', 'hoodie', 'jeans', 'boots', 'sandal',
    'ring', 'necklace', 'bracelet', 'watch', 'earring', 'brooch', 'pin', 'cufflink', 'wallet', 'purse',
    'bag', 'backpack', 'suitcase', 'briefcase', 'umbrella', 'key', 'lock', 'door', 'window', 'mirror',
    'chair', 'table', 'sofa', 'bed', 'pillow', 'blanket', 'sheet', 'mattress', 'closet', 'drawer',
    'shelf', 'cabinet', 'lamp', 'light', 'fan', 'heater', 'air', 'conditioner', 'oven', 'stove',
    'microwave', 'fridge', 'freezer', 'dishwasher', 'toaster', 'blender', 'mixer', 'grill', 'kettle', 'fryer',
    'sink', 'faucet', 'shower', 'bathtub', 'toilet', 'soap', 'towel', 'brush', 'comb', 'razor',
    'shampoo', 'conditioner', 'toothpaste', 'floss', 'lotion', 'cream', 'perfume', 'deodorant', 'mirror', 'scale',
    'bike', 'car', 'truck', 'bus', 'train', 'plane', 'boat', 'ship', 'subway', 'scooter',
    'skateboard', 'rollerblade', 'helmet', 'seatbelt', 'steering', 'wheel', 'engine', 'tire', 'brake', 'pedal',
    'stop', 'sign', 'traffic', 'light', 'crosswalk', 'sidewalk', 'road', 'street', 'avenue', 'boulevard',
    'highway', 'bridge', 'tunnel', 'parking', 'lot', 'garage', 'station', 'airport', 'dock', 'port',
    'dog', 'cat', 'bird', 'fish', 'turtle', 'frog', 'rabbit', 'hamster', 'mouse', 'rat',
    'horse', 'cow', 'pig', 'sheep', 'goat', 'chicken', 'duck', 'goose', 'turkey', 'deer',
    'bear', 'lion', 'tiger', 'leopard', 'cheetah', 'wolf', 'fox', 'elephant', 'giraffe', 'monkey',
    'ape', 'kangaroo', 'koala', 'panda', 'zebra', 'camel', 'llama', 'ostrich', 'eagle', 'hawk',
    'owl', 'falcon', 'parrot', 'penguin', 'dolphin', 'whale', 'shark', 'octopus', 'jellyfish', 'seal'
]
longest_word = max(words, key=len) # to find the longest word
shortest_word = min(words, key=len) # to find the shortest word
# print(shortest_word)
# print(longest_word)


print("Enter the level of difficulty (easy, medium, hard)")
print(" For Easy, enter 1\n For Medium, enter 2\n For Hard, enter 3\n")



# inputting the level that the player wants to play on
while True:
    level = input("Enter the level: ")
    if level.isdigit():
        level = int(level)
        if level in [1, 2, 3]:
            break
        else:
            print("Please enter a valid level!")
            continue
    else:
        print("Please enter a valid character!")
        continue


# generating a random word based on the level selected
if level == 1:
    maximum_guesses = 20
    print("You have selected Easy level!\n")

    while True:
        random_word = random.choice(words)

        if len(random_word) == 3:
            print("The random word has been generated! It is a 3-letter word.")
            break
        else:
            continue

elif level == 2:
    maximum_guesses = 15
    print("You have selected Medium level!\n")

    while True:
        random_word = random.choice(words)

        if 3< len(random_word) <= 5:
            print(f"The random word has been generated! It is a {len(random_word)}-letter word.")
            break
        else:
            continue

elif level == 3:
    maximum_guesses = 10
    print("You have selected Hard level!\n")

    while True:
        random_word = random.choice(words)

        if len(random_word) > 5:
            print(f"The random word has been generated! It is a {len(random_word)}-letter word.")
            break
        else:
            continue
    

# print(random_word)

random_word_list = list(random_word)
# print(random_word_list)

# Creating underscores based on the length of the random word
display_word = ['_' for _ in range(len(random_word_list))]
print(display_word)

# Showing the underscores
print("Here is the word you need to guess:")
print(" ".join(display_word))  # The underscores represent the letters


guess = 0
incorrect_guess = 0


# making the guess system
while '_' in display_word and incorrect_guess <= maximum_guesses:
    user_guess = input("Enter a character to guess: ").lower()

    if user_guess.isalpha() and len(user_guess) == 1:
        if user_guess in random_word_list:
            print("Congratulations! The letter is in the word! \n")
            for idx, letter in enumerate(random_word_list):
                if letter == user_guess:
                    display_word[idx] = user_guess
            print(" ".join(display_word)) 
            print("\n")
        else:
            incorrect_guess += 1
            print("Sorry, the letter is not in the word! Guess again!! \n")
        
        guess += 1
    else:
        print("Please enter a valid character i.e., aplbhabet!")
        print("And please guess only one letter\n")
        continue

print(incorrect_guess)

if '_' not in display_word:
    print("Congratulations! You have guessed the word correctly!")
    print(f"The word was {random_word}")
    print(f"It took you {guess} guesses to guess the word correctly!")
else:
    print("Game Over! You've run out of guesses.")
    print(f"The word was {random_word}")