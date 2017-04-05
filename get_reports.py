#!/usr/bin/env python
import csv
import sys
import click
import requests
import os.path
from tqdm import tqdm

#Please update this value with your read-only API_KEY
API_KEY = '<YOUR_API_KEY>'

@click.command()
@click.option('--column-index', '-c', default=1, help='Index (starting from 0) of the column hanving incident id. Default: 2')
@click.option('--infile', '-i', default='incidents.csv', help='Dowloaded Reports file location from Pagerduty. Default: incidents.csv' )
@click.option('--outfile', '-o', default='reports.csv', help='Output filename to write with Notes. Default: reports.csv')
def add_notes(column_index, infile, outfile):
    while not os.path.exists(infile):
        infile = click.prompt("Input file doesnot exist. Specify new location")
    if os.path.exists(outfile):
        click.confirm('Output file {} already exits, do you want to overwrite ?'.format(outfile), abort=True)

    with open(infile,'r') as incidents:
        row_count = sum(1 for row in incidents) - 1

    with open(infile,'r') as incidents:
        with open(outfile, 'w') as reports:
            writer = csv.writer(reports, lineterminator='\n')
            reader = csv.reader(incidents)

            all = []
            row = next(reader)
            row.append('Notes')
            all.append(row)

            print "Processing %s rows from file %s." % (row_count, infile)

            for row in tqdm(reader, total=row_count):
                row.append("\n".join(get_notes(row[column_index])))
                all.append(row)
            print "Writing output to file %s." % outfile
            writer.writerows(all)

def get_notes(incident):
    url = 'https://api.pagerduty.com/incidents/' + incident + '/notes'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    r = requests.get(url, headers=headers)
    notes = []
    for note in r.json()['notes']:
        notes.append(note['content'])
    return notes

if __name__ == '__main__':
    add_notes()
