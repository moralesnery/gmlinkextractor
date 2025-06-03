# gmlinkextractor
Small python script utility that scraps coordinate data from a Google Maps shortened link and can run recursively
(For windows)

How to run:
1. Create a CSV file called "source.csv" in the same folder where the python script is located in your computer
2. Add one shortened google map link per line to the file (https://maps.app.goo.gl/HuptUo4n5uJnyEEH6), save it and close it.
3. Run the script (python gmapsextractor.py) and wait for it to finish
4. You will see a new CSV file called "output.csv" in the same folder where "source.csv" and the python script were located.

**TODO**
- Add support for Linux and MacOS
- Add basic GUI
- Add support for CSVs with more than one column (use only the first column if there are more in the file)
- Add a dist folder with executables for Windows / Linux / MacOS.

**This script and its resources are distributed under GPLv2 license. Please check the LICENSE file for more information**
