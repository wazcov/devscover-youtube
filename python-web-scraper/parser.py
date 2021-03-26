from bs4 import BeautifulSoup
import sys
import argparse
import urllib.request

def parseSite(site):
	page = urllib.request.urlopen(site)
	soup = BeautifulSoup(page, 'html.parser')

	name = soup.body.h1.get_text().strip()
	description = soup.find("div", class_="sb-teaser").get_text().strip()
	teamsize = soup.find("i", class_="icon-team").next_sibling.split(" Employees")[0].strip()
	image = soup.find("span", class_="company-logo").find("div").find("img")['src'].strip()
	website = soup.find("label", text="Official Website:").find_next('a')['href'].strip()
	founded = soup.find("i", class_="icon-calendar").next_sibling.strip()
	sectors = soup.find("label", text="Sector:").next_sibling.strip()
	stage = soup.find("label", text="Company Stage:").next_sibling.strip()
	model = soup.find("label", text="Business Model:").next_sibling.strip()

	location = soup.find("i", class_="icon-location").parent.parent.findNext('a').get_text().split(", ")
	city = location[0].strip()
	country = location[1].strip()

	print(f"{image}, {name}, {sectors}, {stage}, {website}, {description[0: 40]}, {model}, {city}, {teamsize}, {country}, {founded}, {description} ")
	print("\n")

def main(argv):
	# define the program description
	text = 'A Python program to parse sites for sciencio platform.'
	# initiate the parser with a description
	parser = argparse.ArgumentParser(description=text)
	parser.add_argument('--file', '-f', required=True,
						help='file of urls to parse')

	# read arguments from the command line
	args = parser.parse_args()

	# Create Headings
	print(f"Background image, Brand Name, Startup Sectors, Startup Stage, Website, High-Concept Pitch, Buisness Model, City, Company Size, Country, Founded, Description ")
	print("\n")

	file = args.file
	if file:
		with open(file) as f:
			lines = f.readlines()
		for line in lines:
			if "/organization/" in line:
				try:
					parseSite(line)
				except Exception as e:
					pass
					#print('Error at %s', 'division', exc_info=e)

if __name__ == "__main__":
	main(sys.argv[1:])