cost = 0
room = input("Which room is vacuum cleaner in? [A/B]: ")
a_dirty = input("Is room A dirty? [T/F]: ")
b_dirty = input("Is room B dirty? [T/F]: ")

if room=="A":
    print("Vacuum Cleaner is in Room A.")
    if a_dirty=="T":
        print("Suck dirt from Room A.\t[+1]")
        cost+=1
        a_dirty="F"
    print("Room A is clean.")
    print("Move to room B.\t[+1]")
    cost+=1
    print("Vaccum cleaner is in room B.")
    if b_dirty=="T":
        print("Suck dirt from room B.\t[+1]")
        cost+=1
        b_dirty="F"
    print("Room B is clean.")

elif room=="B":
    print("Vacuum Cleaner is in Room B.")
    if b_dirty=="T":
        print("Suck dirt from Room B.\t[+1]")
        cost+=1
        b_dirty="F"
    print("Room B is clean.")
    print("Move to room A.\t[+1]")
    cost+=1
    print("Vaccum cleaner is in room A.")
    if a_dirty=="T":
        print("Suck dirt from room A.\t[+1]")
        cost+=1
        a_dirty="F"
    print("Room A is clean.")    

if a_dirty=="F" and b_dirty=="F":
    print("\nBoth Rooms are clean.")
    print("Cost to clean the rooms: ",cost)