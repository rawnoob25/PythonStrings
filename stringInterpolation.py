"""
Illustrates string interpolation
"""
def string_interpolation1():
	medals = 'bronze silver gold'.split()
	for m in medals:
		print('%s_top5.csv'%m, end=" ")
	print()

if __name__=='__main__':
	string_interpolation1()