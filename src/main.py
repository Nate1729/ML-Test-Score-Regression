import csv

def read_data():
	f_path = '../data/data.csv'
	points = []
	with open(f_path, 'r') as f:
		my_reader = csv.reader(f)
		for row in my_reader:
			points.append([float(row[0]), float(row[1])])
	return points

	



		


if __name__ == '__main__':
	print(read_data())