import random

print("Welcome to hangman game")

word_list = ["apple","banana","cherry","strawberry"]

rand_word = random.choice(word_list)

sample_word_array = list(rand_word)

rand_word_array = list(rand_word)

for i in range(len(rand_word_array)):
  rand_word_array[i] = "_"
  hidden_word_array = rand_word_array


hidden_word = ' '.join(hidden_word_array)
print(hidden_word)

sample_word = ' '.join(sample_word_array)


 
lives = 8
while sample_word != hidden_word:

  guess = input("Enter the letter: ").lower()

  if guess in rand_word:

    for i in range(len(rand_word_array)):

      if rand_word[i] == guess:
        hidden_word_array[i] = guess
        hidden_word = " ".join(rand_word_array)
  else:
    lives -= 1
    print("Wrong answer try again")
    print("Remaining lives: ",lives)

  if sample_word == hidden_word:
    print(hidden_word)
    print("You won")
    break

  if lives == 0:
    print("You lost")
    break


  print(hidden_word)
  




