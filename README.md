#L1TRegionDumper

This repository contains a very simple CMSSW analyzer and a configuration file:

plugins/L1TRegionDumper.cc: Dumps CMS Calorimeter Layer-1 Trigger with UCTRegions to the log file in ASCII format

test/testL1TRegionDumper.py: Configures to read RAW data, emulates CMS Calorimeter Layer-1 Trigger starting from unpacked Layer-1 input data recorded in the RAW data to produce new UCTRegions

test/zerobiasRootFiles: List of ZeroBias RAW data files available as of 2022-01-14 in the UW-Madison HDFS
