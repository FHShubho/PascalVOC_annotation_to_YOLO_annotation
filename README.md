# PascalVOC annotation to YOLO annotation

> Python script for converting Pascal VOC XML annotation files to normalized YOLO TXT annotation files 



#### Using the Script

1.  Create a file called <mark>name.txt </mark> with the class names separated by newlines.

2. Put both the  *name.txt* and  *convert.py* files in the folder containing the *XML* annotation files.

3. Run the script

   ```
   python convert.py
   ```
3. If the script run into any invalid xml files, list of the files can be found in *invalid_files.txt*
   

#### PascalVoc XML annotation format example

```xml
<annotation>
	<folder>Images</folder>
	<filename>02_Motijheel_280714_0005.jpg</filename>
	<path>E:\Datasets\Dataset\Images\02_Motijheel_280714_0005.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>1200</width>
		<height>800</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>bus</name>
		<pose>Unspecified</pose>
		<truncated>1</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>833</xmin>
			<ymin>390</ymin>
			<xmax>1087</xmax>
			<ymax>800</ymax>
		</bndbox>
	</object>
	<object>
		<name>bus</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>901</xmin>
			<ymin>284</ymin>
			<xmax>1018</xmax>
			<ymax>395</ymax>
		</bndbox>
	</object>
</annotation>

```



#### Converted YOLO annotation format example

```
0 0.8 0.764375 0.21166666666666667 0.55375
0 0.7995833333333333 0.740625 0.0975 0.77125
```

