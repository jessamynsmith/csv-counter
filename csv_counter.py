#!/usr/bin/env python


# Given a CSV with arbitrary fields:
#   - Find and show 5 most common values in each field, and their counts


import unicodecsv as csv
from collections import Counter


def count_data(infile):
    # Dictionary of counters (will have one for each field in the CSV
    counters = {}
    # E.g.
    # counters = {
    #     Keep track of every occurring value in the row
    #     'Sector': Counter({
    #           'Municipality': 10805,
    #           'School Board': 5010,
    #           'Post-Secondary Institution', 756
    #     }),
    #     'City': Counter({
    #           'Toronto': 1676,
    #           'Ottawa': 539,
    #           'Mississauga', 384
    #     }),
    # }

    with open(infile, "rb") as csv_in:
        reader = csv.DictReader(csv_in, encoding='utf-8')

        # Initialize counters, creating one for each field
        for fieldname in reader.fieldnames:
            counters[fieldname] = Counter()

        # Iterate over lines in CSV
        for row in reader:
            # Iterate over the fields in the row
            for fieldname in row.keys():
                field_value = row[fieldname]
                # Update the counter for this field, incrementing the count for the value from this row
                counters[fieldname][field_value] += 1

    return counters


# If the script is being invoked as main, run the counter functionality
if __name__ == "__main__":

    # Input CSV file
    infile = 'data/bps_raw_data_2013_revised_en.csv'
    counters = count_data(infile)

    # For every counter, print out the top 3
    for fieldname in sorted(counters.keys()):
        print('%s: %s' % (fieldname, counters[fieldname].most_common(5)))
