import re

convert = {
'int': 'int64',
'int64': 'int64',
'bigint': 'int64',
'binary': 'bytes',
'bit': 'bool',
'nvarchar': 'string',
'char': 'string',
'Character': 'string',
'varchar': 'string',
'text': 'string',
'xml': 'string',
'date': 'date',
'datetime': 'datetime',
'datetime2': 'datetime',
'decimal': 'numeric',
'decimal': 'bignumeric',
'float': 'float64',
'money': 'numeric',
'nchar': 'string',
'ntext': 'string',
'numeric': 'numeric',
'numeric': 'bignumeric',
'real': 'float64',
'smalldatetime': 'datetime',
'smallint': 'int64',
'smallmoney': 'numeric',
'time': 'time',
'timestamp': 'timestamp'
}
regrx_pattern ="[$&+,:;=?@#|'<>.-^*()%!]*([0-9])[$&+,:;=?@#|'<>.-^*()%!]"
File_out = "./src/inputfiles_out1.sql"
with open('input\inputfiles.sql', 'r') as f:
    sql_content = f.read()


sql_lines = sql_content.split('\n')


modified_sql_lines = []
for line in sql_lines:
    if 'COLLATE' in line:
        line = line.split('COLLATE')[0].strip()
        print("strip lines")
        print(line)
    # for data_type, new_type in convert.items():
    #     line = line.replace(data_type, new_type)
    #     modified_sql_lines.append(line)
    # print ("modified_sql_lines")
    # print (modified_sql_lines)
    # print('\n')

# modified_sql_content = '\n'.join(modified_sql_lines)
# lines = re.sub(regrx_pattern, ",", modified_sql_content)
# #nvarstring
# # Replace_nvarchar = {"nvarchar" :	"string"}
# # for old_str, new_str in Replace_nvarchar.items():
# #     lines = lines.replace(old_str, new_str)

# with open(File_out, "w") as file:
#     file.write(lines)

# print(lines)
# print("Replacement completed.")

