# 1. შექმენით BMI-ის გამომთვლელი ფუნქცია, რომელიც არამარტო ქულას უპრინტავს მომხმარებელს, არამედ ტექსტურად ეუბნება, თუ რომელ წონით კატეგორიაში არის ის, დავალების შესასრულებლად გამოიყენეთ შემდეგი ფორმულა:
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    # კატეგორიები
    if bmi < 18.5:
        category = "დაბალი წონა"
    elif 18.5 <= bmi < 24.9:
        category = "ნორმალური წონა"
    elif 25 <= bmi < 29.9:
        category = "მოპოები წონა"
    else:
        category = "ჭარბი წონა"

    # მომხმარებელს ვაწვდით შედეგს
    print(f"თქვენი BMI არის: {bmi:.2f}, კატეგორია: {category}")

# მაგალითად გამოსაყენებლად
calculate_bmi(70, 1.75)  # თქვენ უნდა ჩაამატოთ თქვენი წონა და სიმაღლე
# 2. შექმენით ფუნქცია სახელად threeproduct, რომელიც არგუმენტათ იღებს 3 რიცხვს და პრინტავს მათ ნამრავლს.
def threeproduct(a, b, c):
    product = a * b * c
    print(f"სამივე რიცხვის ნამრავლი არის: {product}")

# მაგალითად გამოსაყენებლად
threeproduct(2, 3, 4)  # ნამრავლი: 2 * 3 * 4 = 24
# 3. შექმენით ფუნქცია სახელად greet, რომელიც არგუმენტად იღებს სახელს და პრინტავს მისალმების მესიჯს.
def greet(name):
    print(f"გამარჯობა, {name}! კეთილი იყოს შენი მობრძანება!")

# მაგალითად გამოსაყენებლად
greet("გიორგი")
# 4. შექმენით ფუნქცია სახელად comparison, რომელიც არგუმენტად იღებს 2 რიცხვს და პრინტავს მათ შორის ჩატარებული 4 არითმეტიკული ოპერაციის შედეგს: <,>,<=,>=.
def comparison(num1, num2):
    print(f"{num1} < {num2}: {num1 < num2}")
    print(f"{num1} > {num2}: {num1 > num2}")
    print(f"{num1} <= {num2}: {num1 <= num2}")
    print(f"{num1} >= {num2}: {num1 >= num2}")

# მაგალითად გამოსაყენებლად
comparison(5, 10)
# 5. შექმენით ფუნქცია სახელად agecalc, რომელსაც არგუმენტად გადაეცემა მომხმარებლის ასაკი და პრინტავს, თუ რომელ წელს დაიბადა იგი.
def agecalc(age):
    current_year = 2024  # შეგიძლიათ შეცვალოთ ეს ცვლადი, თუ სხვაგვარი წელი გჭირდებათ
    birth_year = current_year - age
    print(f"თქვენი დაბადების წელი არის: {birth_year}")

# მაგალითად გამოსაყენებლად
agecalc(30)