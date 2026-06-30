Python Automation Script – Table Lineage Extraction


📌 Project Description
At WBD, documenting database tables and their lineage across layers is essential for managing data pipelines. While Colibri supports this process, certain tasks still require manual effort. To streamline documentation, we built a Python automation script that extracts tables from JSON files and traces their lineage — showing how a source table flows through bronze and silver layers until it reaches the gold layer.

This repository provides the script and supporting resources to simplify schema documentation, reduce manual overhead, and ensure accurate tracking of table dependencies and lineage across the data pipeline.

📂 Repository Contents
Python Script – Automates the extraction and lineage tracing.

JSON File – Contains all tables and their lineage information.

Target File – Specifies the source table for which lineage is traced.

⚙️ Steps to Execute
Prepare the folder  
Place all three files —

the Python script

the JSON file (containing tables and lineage)

the target file (specifying the source table)
into a single folder.

Specify the source table  
In the target file, enter the name of the source table for which you want to trace lineage.

Open the command prompt  
Navigate to the folder path where the files are saved.

Run the script  
Execute the following command:

bash
python python_filename.py --graph json_filename.json --target target_filename.txt
View the output  
The script will generate the lineage for the specified source table, showing its flow through bronze and silver layers up to the gold layer (as illustrated in the provided snapshot).

✅ Benefits
Eliminates manual effort in lineage documentation.

Ensures consistency and accuracy across schema structures.

Saves time and reduces errors in large-scale data environments.

Provides clear lineage outputs for better collaboration and pipeline management.
