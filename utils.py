def get_population(data,country):
	register = population_by_country(data,country)
	population_dict = {key[0:4]:int(value) for key,value in register[0].items() if key.startswith("2") or key.startswith("1")}
	labels = population_dict.keys()
	values = population_dict.values()
	return labels,values

def get_column(data, name_column):
	return [data[i][name_column]  for i in range(0,len(data))]


def population_by_country(data,country):
	result = list(filter(lambda item: item["Country/Territory"] == country,data))
	return result