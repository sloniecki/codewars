
def calculate(material):
    total = 0
    cur_max = max(material)

    while cur_max > 0:
        level = []

        for i in range(len(material)):
            if material[i] == cur_max:
                level.append(i + 1)

        if len(level) > 2:
            total += level[-1] - level[0] - len(level) + 1
        elif len(level) == 2:
            total += level[-1] - level[0] - 1
        for i in level:
            material[i - 1] -= 1

        cur_max = max(material)

    return total