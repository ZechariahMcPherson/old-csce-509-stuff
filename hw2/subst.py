#Creator: Gregory Zechariah McPherson

from sys import argv
import re
import os
import sys

def scrub_social_security_numbers(self):
    """"scrubs phone numbers from file"""
    compiledRegex = re.compile("(?<!\S)(\d{3})(-\d{2}-\d{1})(\d{3})(?!\S)")
    afterScrub = compiledRegex.sub(r"\3\2\1", self)

    return afterScrub

def scrub_phonenumbers(self):
    """"scrubs phone numbers from file"""
    afterScrub = re.sub("(\d{3}[-?|\.?]?){1,2}\d{4}(\ ext\ [\d]{3})?(?!\S)", "<phone-number>", self)

    return afterScrub

def scrub_email(self):
    """"scrubs email addresses from file"""
    afterScrub = re.sub("(\S+@[a-zA-z]+\.?[a-z]+?\.[a-z]{3}(?!\S))", "<email>", self)

    return afterScrub

def create_output_file():
    """"creates output file"""
    if os.path.isfile("output.txt"):
        os.remove("output.txt")
    newFile = open("output.txt","w+")

    return newFile

def get_file_contents():
    """"gets the contents of the user given file"""
    script, filename = argv

    if os.path.isfile(filename):
        fileObj = open(filename)
        fileContents = fileObj.read()
        return fileContents
    else:
        sys.exit("Oops! We can't seem to find"+ filename)

def main():
    """"calls the functions needed to scrub and writes the output"""
    writeFile = create_output_file()
    fileContents = get_file_contents()
    fileContents = scrub_email(fileContents)
    fileContents = scrub_phonenumbers(fileContents)
    fileContents = scrub_social_security_numbers(fileContents)

    writeFile.write(fileContents)


main()
