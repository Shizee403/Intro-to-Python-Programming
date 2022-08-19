import traceback
def calculator():
     
    # Get dog age
    dog_age =input("Enter the dog's age:")
 
    try:
        dog_age = float(dog_age)
        dog_age_in_Human_years = 0
        if dog_age>0:
     
          if 0 < dog_age <= 1 :
             dog_age_in_Human_years += dog_age * 15.0
          elif 1 < dog_age <= 2 :
             dog_age_in_Human_years += dog_age * 12.0
          elif 2 < dog_age <= 3 :
             dog_age_in_Human_years += dog_age * 9.3
          elif 3 < dog_age <= 4 :
            dog_age_in_Human_years += dog_age * 8.0
          elif 4 < dog_age <= 5 :
            dog_age_in_Human_years += dog_age * 7.2
          elif dog_age>=6:
            dog_age_in_Human_years += 5 * 7.2 + (dog_age - 5) * 7.0 
          print("The printgiven dog age", dog_age, "is", round(dog_age_in_Human_years, 2), "in human years.")
        else:
          print("Age cannot be a negative number")
 
    except:
        print(dog_age, "is an invalid age.")
        print(traceback.format_exc())
       
    
calculator()