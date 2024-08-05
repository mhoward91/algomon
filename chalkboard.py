from typing import List


def unhappy_friends(
    n: int,
    preferences: List[List[int]],
    pairs: List[List[int]]
) -> int:
    num_unhappy = 0

    curr_partner = dict()
    for id1, id2 in pairs:
        curr_partner[id1] = id2
        curr_partner[id2] = id1

    preferences = [
        {prefs: id_ for id_, prefs in enumerate(pref)} for pref in preferences
    ]

    for i in range(n):
        partner = curr_partner[i]

        if any(
            preferences[par][i] < preferences[par][curr_partner[par]]
                for par in preferences[i]
                [:preferences[i][[partner]]]):
            num_unhappy += 1

    return num_unhappy


def rotting_oranges():
    pass
