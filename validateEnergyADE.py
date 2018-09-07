#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri July 13 11:27:23 2018

@author: kavisha
"""

#Energy ADE Validator

from lxml import etree
import argparse

def argRead(ar, default=None):
    
    """Corrects the argument input in case it is not in the format True/False."""
    if ar == "0" or ar == "False":
        ar = False
    elif ar == "1" or ar == "True":
        ar = True
    return ar


#-------------start of program-------------------#

print ("\n****** Validator for Energy ADE Datasets *******\n")  
argparser = argparse.ArgumentParser(description='******* Validator for Energy ADE Datasets *******')
argparser.add_argument('-i', '--filename', help='CityGML ADE dataset filename', required=False)
argparser.add_argument('-p', '--profile', help='Energy ADE XSD (full/KIT profile)', required=False)
args = vars(argparser.parse_args())

inputFileName = args['filename']
adeProfile = argRead(args['profile'])
if inputFileName:
    inputFile = str(inputFileName)
    print ("CityGML input file: ", inputFile)
else:
    print ("Error: Enter the CityGML Energy ADE test dataset!! ")

if adeProfile == 0:
    adeSchema = "schema/EnergyADE.xsd"
    print ("Using full CityGML Energy ADE schema: ", adeSchema)
    print ()
elif adeProfile == 1:
    adeSchema = "schema/KIT-EnergyADE-Profil.xsd"
    print ("Using KIT profile CityGML Energy ADE schema: ", adeSchema)
    print ()
    
else:
    print ("\nError: Set the ADE Schema option (-p) :  ")
    print ("0: Full CityGML Energy ADE schema ")
    print ("1: KIT profile CityGML Energy ADE schema")
    print ("Program Terminated\n")
    exit()


parser = etree.XMLParser(ns_clean=True)
xml = etree.parse(inputFile)
xsd = etree.parse(adeSchema)
xmlschema = etree.XMLSchema(xsd)
valid = xml.xmlschema(xsd)
if valid == True:
    print ("Dataset is Valid!")
else:
    try:
        xmlschema.assert_(xml)
    except etree.XMLSyntaxError as e:
        print ("PARSING ERROR", e)
    
    except AssertionError as e:
        print ("INVALID DOCUMENT", e)