# 2. Input()-ის გამოყენებით მომხმარებელს შემოატანინეთ მისი სახელი, შემდეგ for loop-ით კი დაპრინტეთ "hello (მომხმარებლის სახელი)" 5 ჯერ.

name=input("your name ?")
for i in range(5):
    print("hello " + name)

# 3. for loop-ის გამოყენებით დაპრინტეთ 20-მდე რიცხვები, თითოეული გაყოფილი 2-ზე.

for i in range(41):
    print(i / 2)

# 4. for loop-ის გამოყენებით დაპრინტეთ 15-მდე რიცხვები, თითოეული გამრავლებული 2-ზე.

for i in range(8):
    print(i * 2)

#5. for loop-ის გამოყენებით დაპრინტეთ 10-მდე რიცხვები, თითოეულის კვადრატი.

for i in range(3):
    print(i * i * i )

#6. for loop-ის გამოყენებით დაპრინტეთ 10-მდე არსებული ყველა რიცხვის ჯამი, ეს ჯამი უნდა შეინახოს for loop-ის გარეთ შექმნილ ცვლად sum-ში.


sum = 0 # იქნება 6-ის ტოლი

for i in range(4):
     sum = sum + i
    
     print(sum)
