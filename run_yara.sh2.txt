#!/bin/bash

echo "Running YARA scan..."
yara64.exe -r "C:\Users\bhc11\Worm-detector\example_rule.yar" "C:\Users\bhc11\Documents"
