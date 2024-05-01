def execute_action(action):
    global hand, on_block, on_table, clear

    if action[0]=="ON":
        if action[1]+"*"+action[2] in on_block:
            return
        else:
            execute_action(["CL",action[2]])
            execute_action(["HL",action[1]])
            print(f"Stack({action[1]},{action[2]})")
            clear.add(action[1])
            clear.remove(action[2])
            on_block.add(action[1]+"*"+action[2])
            hand=None

    elif action[0]=="CL":
        if action[1] in clear:
            return
        else:
            a=action[1]
            b=None
            for item in on_block:
                if a==item[2]:
                    b=item[0]
                    break
            if b is None:
                return
            execute_action(["CL",b])
            execute_action(["ON",b,a])
            execute_action(["AE"])
            hand=b
            print(f"Unstack({b},{a})")
            clear.add(a)
            on_block.remove(b+"*"+a)       
            
    elif action[0]=="ONT":
        if action[1] in on_table:
            return
        else:
            a=action[1]
            b=None
            for item in on_block:
                if a==item[2]:
                    b=item[0]
                    break
            if b is None:
                return
            execute_action(["CL",b])
            execute_action(["ON",b,a])
            execute_action(["AE"])
            hand=b
            print(f"Unstack({b},{a})")
            clear.add(a)
            on_table.add(a)
            on_block.remove(b+"*"+a)      

    elif action[0]=="AE":
        if hand==None:
            return
        else:
            print(f"Putdown({hand})")
            on_table.add(hand)
            hand=None

    elif action[0]=="HL":
        if hand==action[1]:
            return
        else:
            execute_action(["CL",action[1]])
            execute_action(["AE"])
            print(f"Pickup({action[1]})")
            hand=action[1]

initial_state = [['C'],['A','B']]
goal_state = [['C','A','B']]

clear = set()
on_table = set()
on_block = set()
hand = None

print("Initial State: ")
for state in initial_state:
    if len(state)>1:
        for i in range(len(state)-1):
            print(f"On({state[i]},{state[i+1]})")
    print(f"OnTable({state[-1]})")

print("\nGoal State: ")
for state in goal_state:
    if len(state)>1:
        for i in range(len(state)-1):
            print(f"On({state[i]},{state[i+1]})")
    print(f"OnTable({state[-1]})")

print("\nPLAN:")

for state in initial_state:
    clear.add(state[0])
    on_table.add(state[-1])
    for i in range(len(state)-1):
        on_block.add(state[i]+"*"+state[i+1])

for goal in goal_state:
    execute_action(["CL",goal[0]])
    for i in range(len(goal)-2, -1, -1):
        execute_action(["ON",goal[i],goal[i+1]])
    execute_action(["ONT",goal[-1]])
    execute_action(["AE"])