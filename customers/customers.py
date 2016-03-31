#!/usr/bin/python
import sys
import os
import math
import json


class Intercom(object):
	def office_distance(self,latitude,longitude):
		"""Calculates and returns the distance between a customer's location(latitude, longitude)
		and the Dublin's office - predetermined location. """

		#Earth's radius (meters)
		R = 6371000

		#Dublin office location (radians)
		lat_office = math.radians(53.3381985)
		lon_office = math.radians(-6.2592576)

		#Customer location (radians)
		lat_user = math.radians(latitude)
		lon_user = math.radians(longitude)

		#Absolute differences
		delta_lat = math.fabs(lat_user - lat_office)
		delta_lon = math.fabs(lon_user - lon_office)

		#central angle between the two points
		delta_s = math.acos(math.sin(lat_office) * math.sin(lat_user) + math.cos(lat_office) 
			* math.cos(lat_user) * math.cos(delta_lon))

		#Distance from the Dublin office
		distance = R * delta_s

		return distance


	# Read the json file of customers and return the matching ones within distance (km)
	# from Dublin office.
	def match_customers(self,filename, distance):
		"""Returns a dict with the names and user ids of the matching customers, within
		distance (km) from Dublin office, read from the provided text file(json formatted).
		"""
		try:
			f = open(filename, 'rU')
			return f
		except IOError:
			print 'Error: There is no such file or directory.'
			sys.exit(1)

		matched_customers = {}

		#Create a dictionary with the matching customers 
		for line in f:
			user_dict = json.loads(line)

			if self.office_distance(float(user_dict['latitude']), float(user_dict['longitude'])) < (distance * 1000):

				matched_customers[user_dict['user_id']] = user_dict['name']
				
		f.close()
		return matched_customers



	def print_sorted_customers(self,user_dict):
		"""Used to print the matching customers sorted by user id (ascending)"""
		for key in sorted(user_dict.keys()):
			print 'Name: %s, ID: %d' % (user_dict[key], key)



	# def main():
	# 	args = sys.argv[1:]

	# 	if not args:
	# 		print 'usage: You have to specify the file'
	# 		sys.exit(1)

	# 	filename = args[0]
		
	# 	customers = match_customers(filename, 100)

	# 	print_sorted_customers(customers)

	# if __name__ == '__main__':
	#   main()			



