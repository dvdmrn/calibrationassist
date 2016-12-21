from __future__ import division
import os
import csv

#------------------------------------------------
csvpath = 'calibrationLogs.csv'
consoleSys = 'windows'

#------------------------------------------------

def main():

	correctResponses = 0
	trialNumber = 0
	calibrated = False
	blockNumber = 1
	participantID = 0

	
	participantID = raw_input("participant ID: \n")
	print "Callibrate accuracy to ~33%\n" 
	var = raw_input("input 'y' for correct, 'n' for incorrect, and 'new' to initiate a new block\n>")


	while calibrated==False:
		
		trialNumber+=1

		if var=="Y" or var=="y":
			os.system('cls')
			correctResponses+=1
			accuracy = calcAverage(correctResponses,trialNumber)
			 
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			print("| accuracy: "+str(accuracy))
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
		if var=="N" or var=="n":
			os.system('cls')
			accuracy = calcAverage(correctResponses,trialNumber)
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			if accuracy > 0.3 and accuracy < 0.4:
				print("| accuracy: *~"+str(accuracy)+"~*")
			else:
				print("| accuracy: "+str(accuracy))
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
		if var=="new":
			os.system('cls')
			correctResponses = 0
			trialNumber = 0
			blockNumber +=1
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------\n\nNew block!"
		if var == "done":
			exit()
		if var == "reset":
			os.system('cls')
			trialNumber = 0
			correctResponses = 0
			accuracy = 0
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			print("| accuracy: "+str(accuracy))
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
			print("block settings reset!")
		if var == "nuclear option":
			os.system('cls')
			trialNumber = 0
			correctResponses = 0
			block = 0
			accuracy = 0
			print("complete reset")
		if var == "export":
			noiseLevels = raw_input("noise level: ")
			signalLevels = raw_input("signal level: ")
			placement = raw_input("actuator placement: ")
			confirm = raw_input("confirm? (y/n): ")

			if confirm == "y":
				print "    writing to file: `"+csvpath+"`..."
				writeCSV(participantID,noiseLevels,signalLevels,placement)
				print "    Complete!"
		if var == "...":
			print "    commands:\n        y: correct response\n        n: incorrect response\n        new: initiate new block\n        export: export .csv\n        reset: reset the current block (if you made a mistake)\n        nuclear option: complete reset (start again from block 1)\n        done: exit program"


		var = raw_input("[y | n | new | export | ...]\n> ")



def calcAverage(correct,trials):
	return correct/trials

def writeCSV(pID,noise,signal,placement):
	prevCSV = readCSV(csvpath)
	with open(csvpath, 'wb') as csvfile:
	    writer = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for row in prevCSV:
	    	writer.writerow(row)
	    writer.writerow([pID,noise,signal,placement])

def readCSV(csvpath):
	csvSoFar = []
	with open(csvpath) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			csvSoFar.append(row)
		return csvSoFar

#------------------------------------------------


main()	

