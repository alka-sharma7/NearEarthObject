"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    List_NEO =[]
    with open(neo_csv_path,'r') as f:
        Reader =csv.DictReader(f)
        #line_count=0
        #next(Reader)
        for row in Reader:
            #NearEarthObject.designation = row['pdes']
            #List_NEO.append(NearEarthObject.designation)
            #NearEarthObject.name = row['name']
            #List_NEO.append(NearEarthObject.name)
            #NearEarthObject.diameter = row['diameter']
            #List_NEO.append(NearEarthObject.diameter)
            #NearEarthObject.hazardous = row['pha']
            #List_NEO.append(NearEarthObject.hazardous)
            
            neo =NearEarthObject(designation =row['pdes'],name = row['name'],diameter=row['diameter'],hazardous=row['pha'])
            List_NEO.append(neo)
            
            
    return List_NEO
   


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    list_ca=[]
    with open(cad_json_path , 'r') as f:
        json_reader=json.load(f)
        
        for row in json_reader['data']:
            #CloseApproach.designation = str(row[0])
            #list_ca.append(CloseApproach.designation)
            #CloseApproach.time= row[3]
            #list_ca.append(CloseApproach.time)
            #CloseApproach.distance=float(row[4])
            #list_ca.append(CloseApproach.distance)
            #CloseApproach.velocity=float(row[7])
            #list_ca.append(CloseApproach.velocity)
            
            ca= CloseApproach(desination=str(row[0]),time= row[3],distance=float(row[4]),velocity=float(row[7]))
            list_ca.append(ca)
    
    return list_ca
    
