import csv

def read_data():
	f_path = '../data/data.csv'
	points = []
	with open(f_path, 'r') as f:
		my_reader = csv.reader(f)
		for row in my_reader:
			points.append([float(row[0]), float(row[1])])
	return points

def compute_error(line, points):	
	error = 0
	for p in points:
		x = p[0]
		y = p[1]
		error += (y - (line[0] + x*line[1])) ** 2
		return error / len(points)



		


if __name__ == '__main__':
	pass