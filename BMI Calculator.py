def cal(weight, height):
    return round((weight/(height**2)),2)

BMI_list=[]
name_list=[]

for i in range(2):
    name=str(input("Enter your name: "))
    weight=float(input("Enter your weight in kilogram: "))*1
    height=float(input("Enter your height in metres: "))

    BMI = cal(weight, height)

    if BMI <= 17.5:
        bmi = "in danger due to low BMI please visit a docter"
    elif BMI <= 25:
        bmi = "a healthy weight"
    elif BMI <= 30:
        bmi = "in danger due to high BMI due to being obese please visit a doctor"
    elif BMI <= 40:
        bmi = "dangerly obese please conatct a doctor immediately"
    else:
        bmi = "overweight"

    name_list.append(name)
    BMI_list.append(BMI)
    print("\n",name, ",your bmi is", BMI,", you are", bmi,".\n")

print("user names", [name_list],"bmi ", [BMI_list])






