# Simple Quiz Program

score = 0

print("Welcome to the Python Quiz!\n")

# Question 1
print("1. What is the capital of Bangladesh?")
print("a) Dhaka")
print("b) Chattogram")
print("c) Khulna")
answer = input("Your answer: ").lower()

if answer == "a":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is a) Dhaka\n")

# Question 2
print("2. Which keyword is used to create a function in Python?")
print("a) func")
print("b) define")
print("c) def")
answer = input("Your answer: ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) def\n")

# Question 3
print("3. What is the output of print(2 + 3)?")
print("a) 23")
print("b) 5")
print("c) Error")
answer = input("Your answer: ").lower()

if answer == "b":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is b) 5\n")

# Question 4
print("4. Which data type is used to store text?")
print("a) int")
print("b) float")
print("c) str")
answer = input("Your answer: ").lower()

if answer == "c":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is c) str\n")

# Final Score
print("Quiz Finished!")
print("Your score:", score, "/ 4")

if score == 4:
    print("Excellent!")
elif score >= 2:
    print("Good job!")
else:
    print("Keep practicing!")