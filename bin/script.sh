#!/bin/bash

echo "Running python unit tests!!!"
python3 -m unittest

if [ $? = 0 ]; # Checks that the return type is 0, if so continues to run the file
then
    echo "Tests passed :) running python file"
    python3 system_scanner/main.py
else # If the tests return 1 it indicates a fail, so the main file isn't run
    echo "Python unittests failed :( Exiting!"
fi
