#!/usr/bin/python

import wikipedia

actualDrug = input("Enter the non-generic name of the drug: ")

wikipedia.search(actualDrug)

GD = wikipedia.page(actualDrug)

print("Generic Name: " + GD.title)
