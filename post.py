"""
Module:  post.appy
Description:  Sample API program for adding data to the database.

Behavior:   1.  If the key is not found on the database, the record is added.
            2.  If the key is found on the database, nothing is done.

Required:   1.  Metadata specifying schema, table name, and key column name.
            2.  Table Data (List) containing rows (tuples).
            3.  Each tuple must exactly match the database row.
            4.  If you want to run locally with your own Postgres database, see Patrick.


Errors:     1.  If the tuple has too many values, rs.text will return:
                "not all arguments converted during string formatting.
            2.  If the tuple has less values than columns in the table, rs.text will return:
                "list index out of range"

Example:    This code adds three personnel to the personnel table.

Advice:     Run this example against our API running on Heroku.
"""

import requests
import json

# Create json dictionary to hold metadata and table data.
json_dict = {}

# Add metadata that specifies schema and table.
json_metadata = {}
json_metadata["schema"] = "its_a_gas"
json_metadata["table"] = "personnel"
json_metadata["key"] = "personnel_id"
json_dict['metadata'] = json_metadata
print("\njson_dict:", type(json_dict), json_dict)

# Create table data.
table_data = []

# Add a row.
table_row = (2, "Chancey", "Gardner")
table_data.append(table_row)

# Add a row.
table_row = (1, "Tom", "Clancy")
table_data.append(table_row)

# Add a row.
table_row = (9, "Walter", "Issacson")
table_data.append(table_row)

# Add table_data to json dictionary.
json_dict['table_data'] = table_data


json_string = json.dumps(json_dict)
print("\njson.dumps(json_data):", type(json_string), json_string, "\n\n")



url = 'https://its-a-gas.herokuapp.com/insert'  # Using app.py on Heroku, Postgres on AWS.
# url = 'http://127.0.0.1:5000/insert'            # Using app.py and Postgres locally.

res = requests.post(url, json=json_string)

if res is None:
    print("res was null.")
else:
    print("type(res):", type(res))
    print("res:", res)
    print("res.ok:", res.ok)
    print("res.status_code:", res.status_code)
    print("res.reason:", res.reason)
    print("res.text:", res.text)
    print("res.json:", res.json)
    print("dir(res):", dir(res))


