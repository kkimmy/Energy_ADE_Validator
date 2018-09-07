# Energy_ADE_Validator
A python script to validate a [CityGML Energy ADE](http://www.citygmlwiki.org/index.php/CityGML_Energy_ADE) dataset against the XSD schema.


System requirements
---------------------

Python packages:

+ [lxml](http://lxml.de)
+ [argparse](https://docs.python.org/3/library/argparse.html)

### OS and Python version
  
The software has been developed on Mac OSX in Python 3.6, and has not been tested with other configurations.

How to use?
-----------

To validate the Energy ADE dataset, use the following command:

```
python3 validateEnergyADE.py -i /path/to/CityGMLfile/ -p 0/1
```
Note: -p specifies the Energy ADE schema used for validation (0 = full Energy ADE schema and 1 = KIT profile Energy ADE schema)

Conditions for use
---------------------

This software is free to use. You are kindly asked to acknowledge its use by citing it in a research paper you are writing, reports, and/or other applicable materials.