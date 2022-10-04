

# Digital Collection Metadata Assessment and Remediation Project - University of Michigan Library

February 2022 - Present. A pilot project remediating the metadata for the University of Michigan's ["The United States and its Territories, 1870 - 1925: The Age of Imperialism"](https://quod.lib.umich.edu/p/philamer/) digital colleciton.

Further documentation on this project can be found in our [report](https://docs.google.com/document/d/15NfpqtLPfcfQ1oiRX9NhGXweel1XqYJVHg5A7OBwCT4/edit#).
## Authors

- Jackson Huang
- Curtis Hunt   
- Gregory McCollum (gregmcc@umich.edu)




## Workflow

Each step in our process is separated into its own folder in this repository. The description below describes the order, operations, and output of the scripts in each folder.

- **Alma_Crosswalk** contains the whole collections metadata in a MARC (.mrc) file. The alma_to_csv.py script converts this data to a csv, crosswalking them to the same headers as the data held in the DLXS-version of the colleciton metadata, extracting specific MARC fields or joining fields to make them ready for comparison with the DLXS data in the next step. The crosswalked data is held in alma_full.csv.

- In **DIFF**, our diff.py script compares the two versions of the colleciton metadata held in alma_full.csv and dxls_full.csv. Our script matches collection items on their mms id numbers and then loops through each of the item's fields, flagging any differences beween the two (with some stripping away of formatting differences and whitespace). If differences existed between a field value, those fields were written to the matches.csv document. Additionally, because we expected the Alma metadata to be more robust and up-to-date, we flagged in our matches.csv document any field where the length of the DLXS value was longer for further investigation.

- We work with this matches.csv document further in **Building_CheckLists**. In building_checklists.py, we loop through each record in the matches.csv document along with the alma_full.csv and dxls_full.csv documents and developed a "check list" for each metadata attribute in the CheckLists subdirectory, populated by ALMA and DLXS values for each record that was flagged as having a longer DLXS value. These CSVs were uploaded to Google Sheets for manual review by the team. Additionally, a running, consolidated 'best version' CSV was created with field values not DLXS-longer flagged, prefering the ALMA values where any discrepenacy existed.

- **Consolidating_Values** contains an Edited_Sheets subdirectory with the check lists established in the previous step, but with our team's manually reviewed reccomednations included in them. We loop through the best_values.csv and add our new suggested field values from these editied sheets in our merging_best_values.py script. The consolidated version with complete field values is held in the new_full_best_values.csv document.

- The **Catalog_Linking** directory contains scripts that develop a CSV of information inlcuding a search URL for the University of Michigan Library catalog on the basis of the title of each record. Some of the main records for this colleciton in the U of M catalog lack a link to the digital collection item. We used these sheets to manually review the catalog search results in Google Sheets to identify these records without digital colleciton links and adding the catalog identification numbers for the corresponding digital collection items.

- In **Subject Sorting** we develop suggested tags for each record on the basis of place. In our subject_test.py we set up a series of Regular Expressions corresponding to each of the places represented. Our ...


