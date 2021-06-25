import csv
from os import read

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

def gradient_step(line_start, points, learning_rate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for p in points:
		x = p[0]
		y = p[1]
		m_gradient += -(2/N) * (y - (line_start[1]*x + line_start[0]))*x
		b_gradient += -(2/N) * (y - (line_start[1]*x + line_start[0]))
	b_new = line_start[0] - (b_gradient * learning_rate)
	m_new = line_start[1] - (m_gradient * learning_rate)
	line_new = [b_new, m_new]
	return line_new

def gradient_descent_runner(points, line_start, learn_rate, num_iters):
	line = line_start
	for _ in range(num_iters):
		line = gradient_step(line, points, learn_rate)
	return line
		


if __name__ == '__main__':
	# Reading in Data
	points = read_data()
	# Initializing parameters
	b_initial = 0
	m_initial = 0
	learning_rate = 0.0001
	num_iterations = 1000
	line = [b_initial, m_initial]
	# Printing out intial conditions
	print("Starting gradient descent at b={} and m={}, ".format(b_initial, m_initial), end='')
	print("Error {}".format(round(compute_error(line, points), 3)))

	line = gradient_descent_runner(points, line, learning_rate, num_iterations)
	print("After {} iterations b={} and m={}". format(num_iterations,
													round(line[0], 3),
													round(line[1], 3)),
													end='')
	print(" Error {}".format(round(compute_error(line, points), 3)))
	