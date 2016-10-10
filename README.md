csv-counter
===========

Unicode CSV reader example. For every field in the CSV, count the occurrences of each unique value and display the 5 most common.

Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://github.com/<username>/csv-counter.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 via homebrew as well, then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv eggtimer --python=/path/to/python3
    pip install -r requirements.txt
    
Run script:

    python csv_counter.py
