#####Place a CSV file called "source.csv" in the same folder where you run this python script in Windows.
#####Then execute the script with the following command:
#####    python gmapsextractor.py
#####The script will take every line in your CSV and try to get the Marker coordinates from the place pinpointed in every link in the file.
#####The marker coordinates will be saved in a file named "output.csv" in the same folder where "source.csv" was placed.

import requests
import os
import warnings



def get_coordinates(url: str):

    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()

        response_code = response.status_code
        response_body = response.text
        
        if (response_code == 200):
            
            #First substring =================================
            meta_start_marker = "<meta content=\""
            meta_end_marker = "itemprop=\"image\">"
            
            meta_start_index = response_body.find(meta_start_marker)
            if meta_start_index == -1:
                print(f"Error: '{meta_start_marker}' not found in the response.")
                #return
                
            meta_end_index = response_body.find(meta_end_marker, meta_start_index)
            if meta_end_index == -1:
                print(f"Error: '{meta_end_marker}' not found after '{meta_start_marker}'.")
                #return
                
            # Adjust end index to include the marker itself
            if (meta_end_index != -1 and meta_start_index != -1):
                meta_substring = response_body[meta_start_index : meta_end_index + len(meta_end_marker)]
                
            #Second substring =================================
            meta_start_marker = "markers="
            meta_end_marker = "&amp;"
            
            meta_start_index = response_body.find(meta_start_marker)
            if meta_start_index == -1:
                print(f"Error: '{meta_start_marker}' not found in the response.")
                #return
                
            meta_end_index = response_body.find(meta_end_marker, meta_start_index)
            if meta_end_index == -1:
                print(f"Error: '{meta_end_marker}' not found after '{meta_start_marker}'.")
                #return
                
            # Adjust end index to include the marker itself
            if (meta_end_index != -1 and meta_start_index != -1):
                meta_substring_2 = response_body[meta_start_index : meta_end_index + len(meta_end_marker)]
                meta_substring_2 = meta_substring_2.replace("markers=","")
                meta_substring_2 = meta_substring_2.replace("&amp;","")
                meta_substring_2 = meta_substring_2.replace("%2C",",")
            
                print("Marker: " + meta_substring_2)
                return meta_substring_2
                

    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error al ejecutar petición HTTP: {e}")




#### MAIN #####
warnings.filterwarnings("ignore")

try:
    print("Running")
    output_content = ""
    with open("source.csv", 'r', encoding='utf-8', newline='') as csv_file:
            for line in csv_file:
                output_content = output_content + get_coordinates(line.strip()) + "\r\n"
                #print(output_content)
            print("\r\nResults saved in \"output.csv\" file.")
    with open("output.csv", 'w', encoding='utf-8') as file:
        file.write(output_content)
except Exception as e:
    print(f"There was an error while trying to run this script: {e}")