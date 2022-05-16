states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthree': set(['or', 'nv', 'ca']),
    'kfour': set(['nv', 'ut']),
    'kfive': set(['ca', 'az']),
}

def find_best_stations(states_needed):
    final_stations = set()
    while states_needed:
        best_station = None
        covered_states = set()

        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(covered_states):
                covered_states = covered
                best_station = station

        states_needed -= covered_states
        final_stations.add(best_station)

    return final_stations

print(find_best_stations(states_needed))
