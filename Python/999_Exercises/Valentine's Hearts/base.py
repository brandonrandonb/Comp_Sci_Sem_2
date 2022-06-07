import datetime
import random
people_list = ["You are", "U r", "Your Mom is", "Your Dad is", "Your Dog is", "Your Family is", " Your Cousin is", "Angel", "The One", "Your Friend is", "Your Lover is", "Dear"]
comp_list = ["really nice", "really hot", "cute", "sexy", "smart", "lovely"]


num_people = random.randrange(0,len(people_list))
num_comp = random.randrange(0,len(comp_list))

print(people_list[num_people] + " " + comp_list[num_comp])








print()
x = datetime.datetime.now()

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
