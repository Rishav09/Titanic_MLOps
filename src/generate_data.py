import random
import pandas as pd
from datetime import datetime


def generate_random_passenger(id):
    """
    Returns a single Titanic passenger as a single row in a DataFrame
    """

    pick_random = random.uniform(0, 2)
    survived = pick_random >= 1

    if survived:
        print("Survivor added")
    else:
        print("Non-Survivor added")

    if survived:
        unif = random.uniform(0, 1)

        if unif < 109 / 342:
            sex = "male"
        else:
            sex = "female"

        if unif < 136 / 342:
            pclass = 1
        elif unif < 223 / 342:
            pclass = 2
        else:
            pclass = 3

        age = random.uniform(0.42, 80.0)

        if unif < 25 / 100:
            fare = random.uniform(0.0, 12.47)
        elif unif < 50 / 100:
            fare = random.uniform(12.47, 26.0)
        elif unif < 75 / 100:
            fare = random.uniform(26.0, 57.0)
        else:
            fare = random.uniform(57.0, 512.0)

        if unif < 233 / 342:
            parch = 0
        elif unif < (65 + 233) / 342:
            parch = 1
        elif unif < (40 + 65 + 233) / 342:
            parch = 2
        else:
            parch = round(random.uniform(3.0, 5.0))

        if unif < 210 / 342:
            sibsp = 0
        elif unif < (112 + 210) / 342:
            sibsp = 1
        else:
            sibsp = round(random.uniform(2.0, 4.0))

        if unif < 219 / 342:
            embarked = "S"
        elif unif < (93 + 219) / 342:
            embarked = "C"
        else:
            embarked = "Q"

    else:
        unif = random.uniform(0, 1)

        if unif < 468 / 549:
            sex = "male"
        else:
            sex = "female"

        if unif < 80 / 549:
            pclass = 1
        elif unif < 177 / 549:
            pclass = 2
        else:
            pclass = 3

        age = random.uniform(1.0, 74.0)

        if unif < 25 / 100:
            fare = random.uniform(0.0, 7.85)
        elif unif < 50 / 100:
            fare = random.uniform(7.85, 10.5)
        elif unif < 75 / 100:
            fare = random.uniform(10.5, 26.0)
        else:
            fare = random.uniform(26.0, 263.0)

        if unif < 445 / 549:
            parch = 0
        elif unif < (53 + 445) / 549:
            parch = 1
        elif unif < (40 + 53 + 445) / 549:
            parch = 2
        else:
            parch = round(random.uniform(3.0, 6.0))

        if unif < 398 / 549:
            sibsp = 0
        elif unif < (97 + 398) / 549:
            sibsp = 1
        else:
            sibsp = round(random.uniform(2.0, 6.0))

        if unif < 427 / 549:
            embarked = "S"
        elif unif < (75 + 427) / 549:
            embarked = "C"
        else:
            embarked = "Q"

    family_size = sibsp + parch + 1
    is_alone = 1 if family_size == 1 else 0
    event_time = pd.Timestamp.now()

    df = pd.DataFrame({
        "passengerid": [id],
        "sex": [sex],
        "age": [age],
        "pclass": [pclass],
        "fare": [fare],
        "parch": [parch],
        "sibsp": [sibsp],
        "embarked": [embarked],
        "family_size": [family_size],
        "is_alone": [is_alone],
        "event_time": [event_time],
        "survived": [int(survived)]
    })

    return df