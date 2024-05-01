def joint_prob(burglary,earthquake,alarm,john,mary):
    burg = 0.001
    earthq = 0.002

    alarm_burg_earthq = {
        (True, True) : 0.95,
        (True, False): 0.94,
        (False, True): 0.29,
        (False, False):0.001
    }

    john_calls = {
        True : 0.9,
        False: 0.05
    }

    mary_calls = {
        True : 0.7,
        False: 0.01
    }

    p_burglary = burg if(burglary==True) else (1-burg)
    p_earthquake = earthq if(earthquake==True) else (1-earthq)
    p_alarm = alarm_burg_earthq[(burglary,earthquake)] if alarm==True else (1-alarm_burg_earthq[(burglary,earthquake)]) 
    p_john = john_calls[john]
    p_mary = mary_calls[mary]

    return p_burglary*p_earthquake*p_alarm*p_john*p_mary

burglary = True if (input("Burglary occurred [T/F]: ")=="T") else False
earthquake = True if (input("Earthquake occurred [T/F]: ")=="T") else False
alarm = True if (input("Alarm rang [T/F]: ")=="T") else False
john = True if (input("John called [T/F]: ")=="T") else False
mary = True if (input("Mary called [T/F]: ")=="T") else False

probability = joint_prob(burglary,earthquake,alarm,john,mary)

print(f"The probability that [Burglary = {burglary}], [Earthquake = {earthquake}], [Alarm = {alarm}], [John called = {john}], [Mary called = {mary}] is : {probability}")