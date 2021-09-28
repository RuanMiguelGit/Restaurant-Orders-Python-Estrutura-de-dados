import csv


def joao_never_orderd(path_to_file):
    my_dict = dict()
    with open(path_to_file, mode="r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[0] == "joao":
                if item[1] not in my_dict:
                    my_dict[item[1]] = 1
                else:
                    my_dict[item[1]] += 1
    return my_dict


def frequent_ordered(path_to_file):
    my_dict = dict()
    with open(path_to_file, mode="r") as file:
        reader = csv.reader(file)
        value = 0
        for item in reader:
            if item[0] == "arnaldo":
                if item[1] == "hamburguer":
                    if item[1] not in my_dict:
                        my_dict[item[1]] = 1
                    else:
                        my_dict[item[1]] += 1
                    value = my_dict[item[1]]
    return value


def mariaFood(path_to_file):
    my_dict = dict()
    with open(path_to_file, mode="r") as file:
        reader = csv.reader(file)
        max_value = 0
        for item in reader:
            if item[0] == "maria":
                if item[1] not in my_dict:
                    my_dict[item[1]] = 1
                else:
                    my_dict[item[1]] += 1

                if my_dict[item[1]] >= max_value:
                    max_value = my_dict[item[1]]
                    max_key = item[1]
    return max_key


def analyze_log(path_to_file):
    # maria = mariaFood(path_to_file)
    # arnanldo = frequent_ordered(path_to_file)
    joao = joao_never_orderd(path_to_file)
    print(joao)


print(analyze_log("./data/orders_1.csv"))
