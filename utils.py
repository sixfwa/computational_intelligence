def from_csv(file):
    data = []
    with open("{}.csv".format(file), "r") as f:
        content = f.readlines()
        for i in range(3):
            content.pop(0)

    for item in content:
        new_item = item.rstrip()
        new_item = new_item.split(',')
        float_item = [float(x) for x in new_item]
        data.append(float_item)

    return data
