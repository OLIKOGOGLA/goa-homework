#1. შექმენით სია, სადაც გექნებათ 7 სიტყვა, შემდეგ:
name=["nino","masho",'salome','giorgi','lika','nika','dachi']
#* დადებითი ინდექსინგის მეშვეობით გამოიტანეთ მეორე და მესამე სიტყვა.
print(name[1:3])
#* დადებითი ინდექსინგის მეშვეობით გამოიტანეთ მეხუთედან ყველა სიტყვა ბოლომდე.
print(name[4:])
#* უარყოფითი ინდექსინგის მეშვეობით გამოიტანეთ მეორე და მესამე სიტყვა.
print(name[-6:-4])
#* უარყოფითი ინდექსინგის მეშვეობით გამოიტანეთ მეხუთედან ყველა სიტყვა ბოლომდე.
print(name[-3:])
#* უაყოფითი და დადებითი ინდექსინგის, ორივეს მეშვეობით, გამოიტანეთ მესამე ელემენტიდან მეექსვეს ჩათვლით ყველა.
print(name[1:-3])
#* გამოიტანეთ სიის ყველა ელემენტი, დადებითი ინდექსინგის მეშვეობით.
print(name[:])
print(name[0:8])