#We are building a simple weather planner. Under the consideration of a set of variables, our user can be able to determine whether it is suitable to travel.
distance_mi = 4
is_raining = False
has_bike = True          #We define our main variables and assign an integer value for the distance (in meters). The rest are defined by boolean values.   
has_car = False
has_ride_share_app = True

if not distance_mi: #The 'not' operand INVERTS the value of an operand. Therefore, this reads as such: Our initial assignment for distance_mi was a TRUTHY boolean value. 'If not TRUTHY (therefore FALSY), print(False)'
    print(False)    #Logically, this must come first because without distance set, there is no use to proceed with the other details.
elif distance_mi <= 1:
    if not is_raining: 
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)