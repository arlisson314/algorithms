def study_schedule(permanence_period, target_time):
    count = 0

    if not target_time or target_time < 0:
        return None

    for i in permanence_period:
        if not isinstance(i[0], int) or not isinstance(i[1], int):
            return None
        if target_time in range(i[0], i[1] + 1):
            count += 1
    return count
