#!/bin/bash
DATA_FOLDER=$PWD/data
cd util/PaDEL-Descriptor/
java -jar PaDEL-Descriptor.jar -maxruntime -1 -waitingjobs -1 -threads -1 -2d -dir $DATA_FOLDER -file $DATA_FOLDER/features.csv -log -retainorder -maxcpdperfile 0 -removesalt -standardizenitro -detectaromaticity
java -jar PaDEL-Descriptor.jar -maxruntime -1 -waitingjobs -1 -threads -1 -fingerprints -dir $DATA_FOLDER -file $DATA_FOLDER/features2.csv -log -retainorder -maxcpdperfile 0 -removesalt -standardizenitro -detectaromaticity
java -jar PaDEL-Descriptor.jar -maxruntime -1 -waitingjobs -1 -threads -1 -2d -fingerprints -dir $DATA_FOLDER -file $DATA_FOLDER/features3.csv -log -retainorder -maxcpdperfile 0 -removesalt -standardizenitro -detectaromaticity

cd ../../