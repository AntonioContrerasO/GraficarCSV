import utils
import read_csv
import charts


def run():

	data = read_csv.read_csv("./data.csv")
	country = input("Type a country ==> ")

	try:
		labels,values = utils.get_population(data,country)
		charts.generate_bar_chart(labels,values)
	except:
  		print("Something went wrong")
	else:
		print("No country with this name")


	countries = utils.get_column(data,"Country/Territory")
	percentages = utils.get_column(data,"World Population Percentage")

	try:
		charts.generate_pie_chart(countries,percentages)
	except Exception as e:
		print("valio verga")
	else:
		print("valio verga x2")






if __name__ == "__main__":
	run()