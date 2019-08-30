import argparse
import os.path
import json
import operator
import csv

parser = argparse.ArgumentParser()
parser.add_argument('--readFile', required=False, default='playerDB.json', help='name of database')
parser.add_argument('--writeFile', required=False, default='LCVstandings.csv', help='output csv')
args = parser.parse_args()

readFile = args.readFile
writeFile = args.writeFile


if not os.path.exists(readFile):
	raise Exception('file does not exist')

wf = open(writeFile, 'w')
wfWriter = csv.writer(wf, delimiter=',', quotechar='"')
wfWriter.writerow(['No.','Name','Elo Rating'])


db = open(readFile, 'r')
jsonDB = json.load(db)

sorted_db = sorted(jsonDB.items(), key=operator.itemgetter(1))

count = 1
for i in sorted_db[::-1]:
	wfWriter.writerow([str(count),str(i[0]),str(i[1])])
	print(str(count) + '. ' + str(i[0]) + ': ' + str(i[1]))
	count += 1

wf.close()
db.close()
