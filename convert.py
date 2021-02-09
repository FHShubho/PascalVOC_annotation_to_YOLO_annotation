#libraries
import os
import glob
import xml.etree.ElementTree as ET

#current directory
path = os.path.dirname(os.path.realpath(__file__))

#class names
print('Reading class names...')
name_file = open(path+r'\name.txt', 'r')
all_names = name_file.readlines()

count = 0
names = {}
for name in all_names:
    names[name.strip()] = count
    count += 1
#print(names)

#xml files
print('Reading xml files...')
path_1 = path + r'\*.xml'
xml_files = glob.glob(path_1)

total = len(xml_files)
total_count = 0
invalid_files = []

print('Converting...')
for files in xml_files:
    #print(files)
    try: 
        tree = root = ET.parse(files).getroot()

        f_name = os.path.basename(files)
        output = f_name[:-3]
        output = output + 'txt'
        #print(output)

        size = root.find('size')
        #print(float(size[0].text))
        width = float(size[0].text)
        height = float(size[1].text)

        #conversion to YOLO format
        for objects in root.findall('object'):
            class_name = objects.find('name').text
            class_label = names[class_name]
            #print(class_label)

            box = objects.find('bndbox')
            xmin = float(box[0].text)
            ymin = float(box[1].text)
            xmax = float(box[2].text)
            ymax = float(box[0].text)

            x = (xmax + xmin) / (width * 2)
            y = (ymax + ymin) / (height * 2)
            w = (xmax - xmin) / width
            h = (ymax - ymin) / height

            #writing to text file
            with open(path + '\\' + output, 'a+') as output_file:
                output_file.write(' '.join([str(class_label), str(x), str(y), str(w), str(h) + '\n']))
    
        total_count += 1
        print(total_count, 'converted out of', total)

    except:
        print(os.path.basename(files), 'Invalid XML file')
        invalid_files.append(os.path.basename(files)+'\n')
    
print('\nCompleted')
print(total_count, 'files converted successfully\n')

if len(invalid_files) > 0:
    with open(path + '\\' + 'invalid_files.txt', 'a+') as output_file:
        output_file.write(invalid_files)
    print(total - total_count, 'ivalid files')
    print('See invalid file list in invalid_files.txt')
