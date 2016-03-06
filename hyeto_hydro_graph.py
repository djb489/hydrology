#!/usr/bin/env python
"""
The MIT License (MIT)

Copyright (c) [2015] [Daniel J. Burgett]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
--------------------------------------------------------------------------------
Author's Note:

This is just a quick script to make hydrographs and hyetographs on the same
plot. I thought we would benefit from having a program that does it for us
rather than having to drag Excel by the ear through the process.

I'll be happy to answer any questions about this version of the program.
Just email me at djb489@humboldt.edu.

Use it, modify it, and share it!
--------------------------------------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt

file_list = [
            'smith@gasquet.csv',
            'RedwoodCreek@Orick.csv'
            ]

x_label = 'Time'# "string"      label of x axis
y_label = 'Discharge [cfs]'# "string"      label of y axis
x_range =  0,10 #"X_0,X_final" range of x axis
y_range =  0,20 #"y_0,y_final" range of y axis
# Just name the file and the script will do the rest.
#file_name = raw_input("Enter the name of the csv file:  ")
#file_name = 'Smith@Gasquet.csv'

for file_name in file_list:
    f = open(file_name,'r')

# Initializing empty to lists to store our data
# Unlike FORTRAN you can create variables whenever you want. It's great.
    time_list = []
    cfs_list  = []
    inch_list = []

    for lines in f:
    # Splits lines on commas. Very appropriate for a csv
        split_lines = lines.split(',')             # We don't float(splitlines[0])
        time_list.append(split_lines[0])           # because those are times/dates.
        cfs_list.append(float(split_lines[1]))
        #inch_list.append(float(split_lines[2]))

# Plotting
# It turns out matplotlib doesn't like plotting strings, so we have to make a
#   list of integer values to plot with. We'll label the tick marks with values
#   from time_list in order to retain that information.
    x = []
    for i in range(0,len(time_list)):
        x.append(i)
        xTicks = time_list
# Actual plotting functions
    plt.figure(1)
    plt.figure(figsize=(len(x),1/len(x)))
    fig, ax1 = plt.subplots()
    ax1.set_aspect(2)
    ax1.set_xlabel(x_label)
    plt.xticks(x,xTicks)
    plt.xticks(range(0,len(xTicks)),xTicks,rotation = 90)
    ax1.axis([0,len(time_list),0.,max(cfs_list)*1.3+1])
    ax1.set_ylabel(y_label, color = 'b')
    ax1.plot(x,cfs_list,linestyle ='-',marker='.', linewidth = 3.0)
# Second set of data
    ax2 = ax1.twinx() # If the number of data points is the same
    ax2.plot(x,inch_list,linestyle ='-',marker='.', linewidth = 3.0, color = 'k')
    ax2.set_ylabel('Runoff [inches]', color = 'k')
# Setting the range of the axes
    ax2.axis([0,len(inch_list),0,max(inch_list)*1.1])
    plt.yticks(color = 'k')
# Just a bit to make everything fit nicely
    plt.tight_layout()
# Plot will be named after the original file
# This bit drops the last 4 characters (.csv) and replaces them with .png
    name = file_name[0:-4]+'.png'
    plt.savefig(name)

    print 'success'
