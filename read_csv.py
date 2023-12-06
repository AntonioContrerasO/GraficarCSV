import csv

def read_csv(path):
	with open(path,"r") as csvfile:
		reader = csv.reader(csvfile,delimiter=",")
		header = next(reader)

		dict_countries = []


		for row in reader:
			dict_countries.append({header[i]:row[i] for i in range(0,len(header))})

		return dict_countries





if __name__ == "__main__":
	data = read_csv("./data.csv")
