import csv


def joao_never_was_there(path_to_file):
    my_dict = dict()
    no_in = dict()
    with open(path_to_file, mode="r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[2] not in no_in:
                no_in[item[2]] = True
            if item[0] == "joao":
                if item[2] not in my_dict:
                    my_dict[item[2]] = True
    my_set_a = set(my_dict)
    my_set_b = set(no_in)
    diff = my_set_b.difference(my_set_a)
    return diff


def joao_never_orderd(path_to_file):
    my_dict = dict()
    no_in = dict()
    with open(path_to_file, mode="r") as file:
        reader = csv.reader(file)
        for item in reader:
            if item[1] not in no_in:
                no_in[item[1]] = True
            if item[0] == "joao":
                if item[1] not in my_dict:
                    my_dict[item[1]] = 1
                else:
                    my_dict[item[1]] += 1
    my_set_a = set(my_dict)
    my_set_b = set(no_in)
    diff = my_set_b.difference(my_set_a)
    return diff


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
    maria = mariaFood(path_to_file)
    arnanldo = frequent_ordered(path_to_file)
    joao = joao_never_orderd(path_to_file)
    joao_at_home = joao_never_was_there(path_to_file)
    data = [maria, str(arnanldo), joao, joao_at_home]

    with open("data/mkt_campaign.txt", "w") as file:
        writer = csv.writer(file, quotechar=" ")
        for line in data:
            writer.writerow([line])


print(analyze_log("./data/orders_1.csv"))
