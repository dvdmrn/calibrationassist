from __future__ import division
import os
import csv

#----------------------------------------------------------------------
csvpath = 'calibrationLogs.csv'

consoleSys = 'unix' #set to 'windows' or 'unix'

#----------------------------------------------------------------------

#----------------------------------------------------------------------
# main function
# returns: nothing
def main():

	clear = 'clear' 
	correctResponses = 0
	trialNumber = 0
	calibrated = False #for main loop
	blockNumber = 1 
	participantID = 0

	#check os for console formatting
	if consoleSys == 'unix':
		clear = 'cls'

	#Intro setup
	participantID = raw_input("participant ID: \n")
	print "Callibrate accuracy to ~33%\n" 
	var = raw_input("input 'y' for correct, 'n' for incorrect, and 'new' to initiate a new block\n>")

	#main loop---------------------------------------------------
	while calibrated==False:
		
		trialNumber+=1

		#correct
		if var=="Y" or var=="y":
			#refresg screen
			os.system(clear)
			correctResponses+=1
			accuracy = calcAverage(correctResponses,trialNumber)
			 
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			print accuracyFormatting(accuracy)
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
		
		#incorrect
		if var=="N" or var=="n":
			os.system(clear)
			accuracy = calcAverage(correctResponses,trialNumber)
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			print accuracyFormatting(accuracy)
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
		
		#new block
		if var=="new":
			os.system(clear)
			correctResponses = 0
			trialNumber = 0
			blockNumber +=1
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------\n\nNew block!"
		
		#exit program
		if var == "done" or var == "exit":
			exit()

		#resets vars
		if var == "reset":
			os.system(clear)
			trialNumber = 0
			correctResponses = 0
			accuracy = 0
			print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
			print("| accuracy: "+str(accuracy))
			print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
			print("block settings reset!")

		#start again
		if var == "nuclear option":
			confirm = raw_input("Will completely wipe history, are you sure? (y/n): ")
			if (confirm=="y"):
				os.system(clear)
				trialNumber = 0
				correctResponses = 0
				blockNumber = 0
				accuracy = 0
				print " _________\n| block "+str(blockNumber)+" |\n------------------------------------"
				print("| accuracy: "+str(accuracy))
				print "| correct: "+str(correctResponses)+"| trial n: "+str(trialNumber)+"\n"
				print("Complete reset!")

		#exports csv
		if var == "export":
			noiseLevels = raw_input("noise level: ")
			signalLevels = raw_input("signal level: ")
			placement = raw_input("actuator placement: ")
			confirm = raw_input("confirm? (y/n): ")

			if confirm == "y":
				print "    writing to file: `"+csvpath+"`..."
				writeCSV(participantID,noiseLevels,signalLevels,placement)
				print "    Complete!"
		
		#user help
		if var == "...":
			print "    commands:\n        y: correct response\n        n: incorrect response\n        new: initiate new block\n        export: export .csv\n        reset: reset the current block (if you made a mistake)\n        nuclear option: complete reset (start again from block 1)\n        exit: exit program"


		var = raw_input("[y | n | new | export | ...]\n> ")

#----------------------------------------------------------------------
# calcAverage
# calculates an mean.
#
# Int correct
# Int trials
# returns: Float
def calcAverage(correct,trials):
	return correct/trials

#----------------------------------------------------------------------
# writeCSV
# Writes a CSV file
#
# String pID (participant ID)
# String noise (noise level)
# String signal (signal level)
# String placement (placement)
# returns: nothing
def writeCSV(pID,noise,signal,placement):
	prevCSV = readCSV(csvpath)
	with open(csvpath, 'wb') as csvfile:
	    writer = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    for row in prevCSV:
	    	writer.writerow(row)
	    writer.writerow([pID,noise,signal,placement])

#----------------------------------------------------------------------
# readCSV
# Gets contents of a csv
#
# String csvpath (path to .csv)
# Returns: List
def readCSV(csvpath):
	csvSoFar = []
	with open(csvpath) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			csvSoFar.append(row)
		return csvSoFar
#----------------------------------------------------------------------
# accuracyFormatting
# pretty formatting if within a certain scope
#
# Float accuracy
# returns: String
def accuracyFormatting(accuracy):
	if accuracy > 0.29 and accuracy < 0.4:
		return "| accuracy: *~"+str(accuracy)+"~*"
	else:
		return "| accuracy: "+str(accuracy)

#----------------------------------------------------------------------


main()	

