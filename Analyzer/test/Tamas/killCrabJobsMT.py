import sys, os
from optparse import OptionParser
from threading import Thread

parser = OptionParser(usage="Usage: python3 %prog codeVersion")
(opt,args) = parser.parse_args()

datasetList = []

codeVersion = sys.argv[1]
#just the number, like 18p2

for fname in os.listdir("crab_projects") :
  if (codeVersion in fname) :
    datasetList.append("crab_projects/"+fname)

for dataset in datasetList:
  outTask = "crab kill -d "+dataset
  os.system(outTask)
