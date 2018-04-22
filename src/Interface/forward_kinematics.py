
from sympy import *
import numpy as np




a = 10   #not too sure about this 
b = 72
c = 150.5
d = 75
e = 155
f = 135
g = 113
h = 105


def forward_kinematics(q1, q2, q3, q4, q5, x, y, theta):

	global a, b, c, d, e, f, g, h

	t = [0, np.deg2rad(q1), np.deg2rad(q2 - 90), np.deg2rad(q3), np.deg2rad(q4), np.deg2rad(90), 0, np.deg2rad(q5)]
	dr = [b, d, 0, 0, 0, 0, 0, h]
	ar = [-c, a, e, f, g, 0, 0, 0]
	alpha = [0, np.deg2rad(-90), 0, 0, 0, 0, np.deg2rad(90), 0]


	Rotz = np.matrix([[cos(t[0]), -sin(t[0]), 0, 0], [sin(t[0]), cos(t[0]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[0]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[0]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[0]), -sin(alpha[0]), 0], [0, sin(alpha[0]), cos(alpha[0]), 0], [0, 0, 0, 1]])
	TR0 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[1]), -sin(t[1]), 0, 0], [sin(t[1]), cos(t[1]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[1]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[1]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[1]), -sin(alpha[1]), 0], [0, sin(alpha[1]), cos(alpha[1]), 0], [0, 0, 0, 1]])
	T01 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[2]), -sin(t[2]), 0, 0], [sin(t[2]), cos(t[2]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[2]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[2]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[2]), -sin(alpha[2]), 0], [0, sin(alpha[2]), cos(alpha[2]), 0], [0, 0, 0, 1]])
	T12 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[3]), -sin(t[3]), 0, 0], [sin(t[3]), cos(t[3]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[3]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[3]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[3]), -sin(alpha[3]), 0], [0, sin(alpha[3]), cos(alpha[3]), 0], [0, 0, 0, 1]])
	T23 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[4]), -sin(t[4]), 0, 0], [sin(t[4]), cos(t[4]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[4]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[4]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[4]), -sin(alpha[4]), 0], [0, sin(alpha[4]), cos(alpha[4]), 0], [0, 0, 0, 1]])
	T3D1 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[5]), -sin(t[5]), 0, 0], [sin(t[5]), cos(t[5]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[5]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[5]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[5]), -sin(alpha[5]), 0], [0, sin(alpha[5]), cos(alpha[5]), 0], [0, 0, 0, 1]])
	TD1D2 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[6]), -sin(t[6]), 0, 0], [sin(t[6]), cos(t[6]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[6]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[6]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[6]), -sin(alpha[6]), 0], [0, sin(alpha[6]), cos(alpha[6]), 0], [0, 0, 0, 1]])
	TD24 = Rotz * Transz * Transx * Rotx


	Rotz = np.matrix([[cos(t[7]), -sin(t[7]), 0, 0], [sin(t[7]), cos(t[7]), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Transz = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, dr[7]], [0, 0, 0, 1]])
	Transx = np.matrix([[1, 0, 0, ar[7]], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
	Rotx = np.matrix([[1, 0, 0, 0], [0, cos(alpha[7]), -sin(alpha[7]), 0], [0, sin(alpha[7]), cos(alpha[7]), 0], [0, 0, 0, 1]])
	T4T = Rotz * Transz * Transx * Rotx


	TWR = np.matrix([[cos(np.deg2rad(theta)), sin(np.deg2rad(theta)), 0, x], [-sin(np.deg2rad(theta)), cos(np.deg2rad(theta)), 0, y], [0, 0, 1, 0], [0, 0, 0, 1]])

	TR1 = TR0 * T01
	TR2 = TR0 * T01 * T12
	TR3 = TR0 * T01 * T12 * T23
	TR4 = TR0 * T01 * T12 * T23 * T3D1 * TD1D2 * TD24
	TRT = TR0 * T01 * T12 * T23 * T3D1 * TD1D2 * TD24 * T4T
	TWT = TWR * TRT
	tipPos_robot = TRT[0:3, 3]
	tipPos_world = TWT[0:3, 3]

	return tipPos_world


print(forward_kinematics(0, 0, 0, 0, 0, 0, 0, 0))
