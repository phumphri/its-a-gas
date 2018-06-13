

from requests.models import Response
import psycopg2
import pandas as pd
import numpy as np
import math
import socket
import os
import json
import flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)



# Assigning the Flask framework.
app = Flask(__name__)


def connect_to_postgres():
    hostname = socket.gethostname()
    print("\nsocket.hostname():", hostname)
    print("os.environ['LOCAL_POSTGRES]:", os.environ['LOCAL_POSTGRES'])
    try:
        if (hostname == 'XPS'):
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.')
            return conn
        elif (hostname == 'DESKTOP-S08TN4O'):  
            conn = psycopg2.connect(os.environ['LOCAL_POSTGRES'])
            print('Connection okay.')
            return conn
        else:
            conn = psycopg2.connect(os.environ['AWS_POSTGRES'])
            print('Connection okay.')
            return conn
    except Exception as e:
        print('Connection failed:', e)


@app.route("/")
def home():
    return render_template("index.html")



@app.route('/domesticautos', methods=['POST', 'GET'])
def domesticautos():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.domesticautos"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            table_data = cur.fetchall()
            print("Fetch All Okay")

            
            # Create json dictionary to hold metadata and table data.
            json_dict = {}

           # Add metadata that specifies schema and table.
            json_metadata = {}
            json_metadata["schema"] = "its_a_gas"
            json_metadata["table"] = "domesticautos"
            json_metadata["key"] = "month, year"
            json_metadata["colmns"] = ["month", "year", "volume", "combined_volume", "adjusted_volume", "sales"]
            json_dict['metadata'] = json_metadata
 
            # Add table_data to json dictionary.
            json_dict['table_data'] = table_data

            json_object = jsonify(json_dict)
            print("jsonify Okay")

            return json_object

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return rows

    if request.method == 'POST':

        json_string = request.get_json(silent=True)

        json_dict = json.loads(json_string)

        json_metadata = json_dict['metadata']

        print("schema:", json_metadata['schema'])
        print("table:", json_metadata['table'])
        # print("table_data", json_dict['table_data'])
    
        status_message = ""

        if json_metadata['schema'] != "its_a_gas":
            status_message = "Inncorrect schema in metadata. "
            status_message += "Expected its_a_gas.  "
            status_message += "Found "
            status_message += json_metadata['schema']
            status_message += "."
            return status_message

        if json_metadata['table'] != "domesticautos":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected domesticautos.  "
            status_message += "Found "
            status_message += json_metadata['table']
            status_message += "."
            return status_message

        sql = "insert into " + json_metadata['schema'] + "." + json_metadata['table'] + " "

        sql += "values ( "


        for i in range(len(json_dict['table_data'][0]) - 1):
            sql += "%s, "

        sql += "%s) "
            
        sql += "on conflict (" + json_metadata['key'] + ") do nothing; "

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.executemany(sql, json_dict['table_data'])
            print('Execute Many Okay.')

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

            conn.commit()
            print('Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return status_message        
    
    return "The inserert was not method POST"

@app.route('/personnel', methods=['POST', 'GET'])
def personnel():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.personnel"

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.execute(sql)
            print('Execute Okay.')

            rows = cur.fetchall()
            print("Fetch All Okay")

            rows = jsonify(rows)
            print("jsonify Okay")

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

        except Exception as e:
            print('Execute Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return rows

    if request.method == 'POST':

        json_string = request.get_json(silent=True)

        json_dict = json.loads(json_string)

        json_metadata = json_dict['metadata']

        print("schema:", json_metadata['schema'])
        print("table:", json_metadata['table'])
        # print("table_data", json_dict['table_data'])
    
        status_message = ""

        if json_metadata['schema'] != "its_a_gas":
            status_message = "Inncorrect schema in metadata. "
            status_message += "Expected its_a_gas.  "
            status_message += "Found "
            status_message += json_metadata['schema']
            status_message += "."
            return status_message

        if json_metadata['table'] != "personnel":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected personnel.  "
            status_message += "Found "
            status_message += json_metadata['table']
            status_message += "."
            return status_message

        sql = "insert into " + json_metadata['schema'] + "." + json_metadata['table'] + " "

        sql += "values ( "


        for i in range(len(json_dict['table_data'][0]) - 1):
            sql += "%s, "

        sql += "%s) "
            
        sql += "on conflict (" + json_metadata['key'] + ") do nothing; "

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        try:
            cur = conn.cursor()
            print('Cursor okay.')

            cur.executemany(sql, json_dict['table_data'])
            print('Execute Many Okay.')

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

            conn.commit()
            print('Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return status_message        
    
    return "The inserert was not method POST"

if __name__ == "__main__":
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
    
    if (hostname == 'XPS'):
        app.run(debug=True)
    elif (hostname == 'DESKTOP-S08TN4O'):  
        app.run(debug=True)
    else:
        from os import environ
        print("Port", environ.get("PORT", "Not Found"))
        app.run(debug=False, host='0.0.0.0', port=int(environ.get("PORT", 5000)))

