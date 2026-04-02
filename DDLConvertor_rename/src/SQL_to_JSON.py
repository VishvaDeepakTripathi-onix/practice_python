import json
# import csv 
# import os
# import sys
# import yaml



# 1. Open and read the file
file_path = '.src/inputfiles.sql'  # Replace with the path to your file
with open('./src/inputfiles.sql', 'r') as file:
    file_contents = file.read()
    print(file_contents)

# 2. Parse the file content into a Python data structure (assuming the content is in a dictionary-like format)
try:
    data_dict = json.loads(file_contents)
    
    # If the file contains JSON data, data_dict will be a Python dictionary.
    
    # 3. Serialize the data structure back to JSON (optional, but can be useful for formatting)
    json_string = json.dumps(data_dict, indent=4)

    # Print the resulting JSON string
    print(json_string)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")


# db_tbl_name ='APVMAS'
# #created empty list for storing temp_file content 
# column_result_db = []

# column_result_table = []

# column_result_col = []

# column_result_datatype = [] 

# #temp_file path stored in varible 

# var_query_1_output_file='D:\Python\DDLConvertor\src\inputfiles.sql'
# #opened the file as read mode and append the content of the file with delimiter as pipe(|) into the list which we created
# with open(var_query_1_output_file, 'r') as f:
#     file_reader = csv.reader(f, delimiter=',')
#     for row in file_reader:
#         #dbname appended in the list
#         column_result_db.append(row[0])
#         #table name appended in the list
#         column_result_table.append(row[1])
#         #col name appended in the list
#         column_result_col.append(row[2])
#         #converted datatype appended in the list
#         column_result_datatype.append(row[3])
# # printing the list using loop
# for x in range(len(column_result_db)):
# 	print(*column_result_db[x], sep ="\n")

#appended the contents of the list in the below json file with creation operation and required formattings
# with open("/src/db_mapping/config/{}.json".format(db_tbl_name),"w") as file_writer:
#     file_writer.write('{\n\t')
#     file_writer.write('"db":'+'"'+column_result_db[0]+'",\n\t')
#     file_writer.write('"tbl_nm":'+'"'+column_result_table[0]+'",\n\t')
#     file_writer.write('"col_list":[\n')
    
#     for co11,col2 in zip(column_result_col, column_result_datatype):
#         file_writer.write('\t\t\t{\n\t\t\t"column_name" :"'+co11+'",\n\t\t\t')
#         file_writer.write('"datatype" :"'+col2+'"\n\t\t\t},\n')
#     file_writer.write('\t\t\t{\n\t\t\t"column_name":"load_date",\n\t\t\t"datatype":"date"\n\t\t\t},')
#     file_writer.write('\n\t\t\t{\n\t\t\t"column_name":"batch_id",\n\t\t\t"datatype":"bigint"\n\t\t\t}')
#     file_writer.write('\n\t\t\t],\n')
#     #deleted the lists for memory release 
# del column_result_db,column_result_table,column_result_col,column_result_datatype
