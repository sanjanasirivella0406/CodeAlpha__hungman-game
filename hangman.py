import random

words = ["python", "school", "banana", "orange", "coding"]

word = random.choice(words)

display_word = []
for letter in word:
    display_word.append("_")

wrong_guesses = 0
max_wrong = 6

guessed_letters = []
wrong_letters = []

print("🎮 ===== WELCOME TO HANGMAN GAME ===== 🎮")
print("🧠 Guess the word one letter at a time!")
print("⚠️ You have only 6 wrong chances.\n")

while wrong_guesses < max_wrong and "_" in display_word:

    print("🔤 Word:", " ".join(display_word))
    print("✅ Correct Letters:", " ".join(guessed_letters))
    print("❌ Wrong Letters:", " ".join(wrong_letters))
    print("❤️ Chances Left:", max_wrong - wrong_guesses)

    guess = input("\n👉 Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("🚫 Please enter only ONE alphabet letter.\n")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("🔁 You already guessed that letter. Try another one!\n")
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("🎉 Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_letters.append(guess)
        wrong_guesses += 1
        print("😢 Wrong guess!\n")

if "_" not in display_word:
    print("🏆🎉 Congratulations! You WON!")
    print("🎯 The word was:", word)
else:
    print("💔😵 Game Over! You LOST!")
    print("🎯 The word was:", word)