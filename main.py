import os
import random



def get_random_number():
    random_words = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'word_list.csv')

    with open(csv_path, newline='', encoding='utf-8') as f:
        for row in f:
            random_words.append(row.strip())

    n = random.randint(0,len(random_words) - 1)
    word = random_words[n]
    letter_amount = len(word)
    return word, letter_amount

def get_model_stages():
    stages = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    txt_path = os.path.join(base_dir, 'models.txt')

    with open(txt_path, encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 7):
            stage = ''.join(lines[i:i+7])
            stages.append(stage)

    return stages




def main():
    word, letter_amount = get_random_number()
    stages = get_model_stages()
    game_over = False
    temp_word = "_"*letter_amount
    i = 0
    
    while not game_over:

        if i >= len(stages) - 1:
            print("Game over")
            print(stages[-1])
            print("Word was:", word)
            game_over = True
            break
        print(stages[i])

        print(' '.join(temp_word))
        answer = input("Letter: ").lower()

        if answer in word:
            d = word.rfind(answer)
            if d != -1 and temp_word[d] == "_":
                temp_word = temp_word[:d] + answer + temp_word[d+1:]
                if "_" not in temp_word:
                    print("You win!")
                    print("Word:", word)
                    game_over = True
        else:
            i += 1         
main()