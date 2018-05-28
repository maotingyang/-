# -*- coding: utf-8 -*-
"""
範圍0~100的猜數字遊戲
"""
head = 0
tail = 100
guess = ""
number =(input("Please think of a number between 0 and 100!"))

while guess != "c":
    answer = round((head+tail)/2)
    print("Is your secret number "+str(answer)+"?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if guess =="h":
       tail = answer
              
    elif guess == "l":
        head = answer
        
    elif guess == "c":
        print("Game over. Your secret number was: "+str(answer))
   
    else:
        print("Sorry, I did not understand your input.")
        

