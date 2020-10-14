# Problem Set 3

## Completed by Alexander Pillai

## Copy of the assignment problems
1. Write a script (or Jupyter Notebook code block) that opens the file, uses a for loop to read through the file line by line and reports the highest water level and the date and time that was observed.
1. Either in a new script or modifying the above script, calculate the lowest, highest and average water level observed during the time period. As above, print the date and time for the lowest and highest readings.
1. Write a script (or Jupyter Notebook) that calculates the fastest rise in water level per 6-minute period between measurements (for this assignment, assume that each line of the dataset is a 6-minute interval) and reports the date and time that was observed and the change in water level from the previous recording.
1. Imagine that the file is providing live readings of the water level. Write a script (or Jupyter Notebook) to print a line of text with a warning if any of these events occur:
    * The water level increases more than 0.25 since the previous recording.
    * The water level is over 5.0.
    * No reading is received at a time point.

## The dataset
The dataset is at: `/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv`
 * The data can also be found in the [class repository](https://github.com/CompTools/Class_Files/blob/master/data/CO-OPS__8729108__wl.csv).
 * The metadata can be found [here](https://github.com/CompTools/Class_Files/blob/master/data/CO_OPS__wl_file.md).

## My submission
I have provided my answers as both a Jupyter Notebook (`answers_notebook.ipynb`) and a Python script (`answers_script.py`).

NOTE: When running the script on the command line, I suggest using `python3 answers_script.py | less` to ensure that you can see the output more clearly.
