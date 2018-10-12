################################################################################
# PART #1
################################################################################
import csv
import pandas as pd

wordcount = {}

def countWordsUnstructured(filename):
    file = open(filename)
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return(wordcount)
    
# Test your part 1 code below.
    
countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Trump_2017.txt')

################################################################################
# PART 2
################################################################################
    
def generateSimpleCSV(targetfile,wordCounts): 
    with open (targetfile,'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])
        for key, value in wordCounts.items():
            csv_writer.writerow([key,value])
    csv_file.close()
    return(csv_file)
    
generateSimpleCSV('wordcounts.csv', wordcount)

    
################################################################################
# PART 3
################################################################################
import os
from os import listdir
from os import chdir

def countWordsMany(directory): 
    dir_list = os.listdir(directory)
    wordCountDict = {}
    for file in dir_list:
        eachWordCount = countWordsUnstructured(file)
        wordCountDict[file] += eachWordCount
    return wordCountDict
 

countWordsMany
# Test your part 3 code below

################################################################################
# PART 4
################################################################################
# def generateDirectoryCSV(wordCounts, targetfile): 
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
# Test your part 4 code below
    
################################################################################
# PART 5
################################################################################
# def generateJSONFile(wordCounts, targetfile): 
    # This function should create an containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data
    
# Test your part 5 code below

################################################################################
# PART 6
################################################################################
# def searchCSV(csvfile, word): 
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# def searchJSON(JSONfile, word): 
    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word
    
# Test your part 6 code to find which file has the highest count of a given word

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value