

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
from flask_cors import CORS


# Assigning the Flask framework.
app = Flask(__name__)
CORS(app)

def connect_to_postgres():
    hostname = socket.gethostname()
    print("socket.hostname():", hostname)
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


@app.route('/manufacturer', methods=['POST', 'GET', 'DELETE'])
def manufacturer():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.manufacturer"

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
            json_metadata["table"] = "manufacturer"
            json_metadata["key"] = "model_id"
            json_metadata["columns"] = [
                "model_id", 
                "model_make_id",
                "model_name",
                "model_trim",
                "model_year",
                "model_body",
                "model_engine_postition",
                "model_engine_cc",
                "model_engine_cyl",
                "model_engine_type",
                "model_engine_values_per_cyl",
                "model_engine_power_ps",
                "model_engine_power_rpm",
                "model_engine_torque_nm",
                "model_engine_torque_rpm",
                "model_engine_bore_mm",
                "model_engine_stroke_mm",
                "model_engine_compression",
                "model_engline_fuel",
                "model_top_speed_kph",
                "model_0_to_100_kph",
                "model_drive",
                "model_transmission_type",
                "model_seats",
                "model_doors",
                "model_weight_kg",
                "model_length_mm",
                "model_width_mm",
                "model_height_mm",
                "model_wheelbase_mm",
                "model_lkm_hwy",
                "model_lkm_mixed",
                "model_lkm_city",
                "model_fuel_cap_l",
                "model_sold_in_us",
                "model_co2",
                "model_make_display",
                "make_display",
                "make_country"]
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
    
        status_message = ""

        if json_metadata['schema'] != "its_a_gas":
            status_message = "Inncorrect schema in metadata. "
            status_message += "Expected its_a_gas.  "
            status_message += "Found "
            status_message += json_metadata['schema']
            status_message += "."
            return status_message

        if json_metadata['table'] != "manufacturer":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected manufacturer.  "
            status_message += "Found "
            status_message += json_metadata['table']
            status_message += "."
            return status_message

        sql = "insert into its_a_gas.manufacturer "

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
            print('Execute Many Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        # Initcap model_make_id. 
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

            sql = "update its_a_gas.manufacturer set model_make_id = initcap(model_make_id); "
            cur.execute(sql)
            print('Execute Initcap Okay.')

            conn.commit()
            print('Initcap Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        # Upper model_make_id. 
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

            sql = "update its_a_gas.manufacturer set model_make_id = upper(model_make_id) "
            sql += "where model_make_id in ('Bmw', 'Gmc'); "
            cur.execute(sql)
            print('Execute Upper Okay.')

            conn.commit()
            print('Third Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close

        return status_message        
    
    if request.method == 'DELETE':

        sql = "delete from its_a_gas.manufacturer"

        status_message = sql

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

            cur.execute(sql)
            print('Execute Delete Okay.')

            status_message = cur.statusmessage
            print("cur.statusmessage:", status_message)

            conn.commit()
            print('Delete Commit Okay.')

        except Exception as e:
            print('Execute Many Failed', str(e))
            return str(e)

        finally:
            if conn is not None:
                conn.close
 
        return status_message        
    
    return "The request.method was not method POST, GET, or DELETE."


@app.route('/foreignlighttrucks', methods=['POST', 'GET'])
def foreignlighttrucks():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.foreignlighttrucks"

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
            json_metadata["table"] = "foreignlighttrucks"
            json_metadata["key"] = "month, year"
            json_metadata["columns"] = [
                "month", 
                "year", 
                "volume", 
                "combined_volume", 
                "adjusted_volume", 
                "sales"]
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

        if json_metadata['table'] != "foreignlighttrucks":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected foreign.  "
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
    
    return "Invalid method:  " + request.method


@app.route('/domesticlighttrucks', methods=['POST', 'GET'])
def domesticlighttrucks():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.domesticlighttrucks"

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
            json_metadata["table"] = "domesticlighttrucks"
            json_metadata["key"] = "month, year"
            json_metadata["columns"] = [
                "month", 
                "year", 
                "volume", 
                "combined_volume", 
                "adjusted_volume", 
                "sales"]
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

        if json_metadata['table'] != "domesticlighttrucks":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected domesticlighttrucks.  "
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
    
    return "Invalid method:  " + request.method


@app.route('/foreignautos', methods=['POST', 'GET'])
def foreignautos():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.foreignautos"

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
            json_metadata["table"] = "foreignautos"
            json_metadata["key"] = "month, year"
            json_metadata["columns"] = [
                "month", 
                "year", 
                "volume", 
                "combined_volume", 
                "adjusted_volume", 
                "sales"]
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

        if json_metadata['table'] != "foreignautos":
            status_message = "Inncorrect table in metadata. "
            status_message += "Expected foreignautos.  "
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
            json_metadata["columns"] = [
                "month", 
                "year", 
                "volume", 
                "combined_volume", 
                "adjusted_volume", 
                "sales"]
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


@app.route('/sales_rollup', methods=['GET'])
def sales_rollup():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.sales_rollup"

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
            json_metadata["table"] = "sales_rollup"
            json_metadata["columns"] = ["year", "volume", "sales"]
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

    
    return "The request.method was not method GET"


@app.route('/models_offered_by_year', methods=['GET'])
def models_offered_by_year():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.model_view"

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
            json_metadata["table"] = "model_view"
            json_metadata["columns"] = ["model_year", "model_body", "models_offered"]
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
    
    return "The request.method was not method GET"

@app.route('/mpg', methods=['GET'])
def mpg():

    if request.method == 'GET':

        conn = None
        conn = connect_to_postgres()
        if conn is None:
            print("Database Connection Failed.")
            return "Database Connection Failed"
        else:
            print("Database Connection Okay.")

        sql = "select * from its_a_gas.mpg_view"

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
            json_metadata["table"] = "mpg_view"
            json_metadata["columns"] = ["model_year", "model_make_id", "mpg_city", "mpg_hwy"]
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
    
    return "The request.method was not method GET."


@app.route('/gdp', methods=['GET'])
def gdp():

    if request.method == 'GET':

        # Create json dictionary to hold metadata and table data.
        json_dict = {}

        # Add metadata that specifies schema and table.
        json_metadata = {}
        json_metadata["schema"] = "its_a_gas"
        json_metadata["table"] = "gdp"
        json_metadata["columns"] = ["Year", "Real_GDP_Trillions"]
        json_dict['metadata'] = json_metadata

        table_data = [
            [2007, 14.874],
            [2008, 14.83],
            [2009, 14.419],
            [2010, 14.784],
            [2011, 15.021],
            [2012, 15.355],
            [2013, 15.612],
            [2014, 16.013],
            [2015, 16.472],
            [2016, 16.716],
            [2017, 17.096]]

        # Add table_data to json dictionary.
        json_dict['table_data'] = table_data

        json_object = jsonify(json_dict)
        print("jsonify Okay")

        return json_object        

    return "The request.method was not method GET."









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

