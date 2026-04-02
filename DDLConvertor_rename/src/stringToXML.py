import xml.etree.ElementTree as ET
# string need to convert into xml with folowing structure. 
# <Table Name> </Table Name>
# <Column Name> </Column Name>
# <Data Type> </Data Type>
# <Size> </Size>
# <Null Constraints> </Null Constraints> 
# <PK> </PK>
# <FK> </FK>
# <SK> </SK>

def convert_to_xml_method1(data_str):
    root = ET.fromstring(data_str)
    return ET.tostring(root, encoding='unicode')