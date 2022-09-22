
# University of Michigan Library Digital Collection Metadata Assessment and Remediation Project

February 2022 - Present. A pilot project remediating the metadata for the University of Michigan's ["The United States and its Territories, 1870 - 1925: The Age of Imperialism"](https://quod.lib.umich.edu/p/philamer/) digital colleciton.

Further documentation on this project can be found in our [final report](https://docs.google.com/document/d/15NfpqtLPfcfQ1oiRX9NhGXweel1XqYJVHg5A7OBwCT4/edit#).
## Authors

- Jackson Huang
- Curtis Hunt
- Gregory McCollum




## Workflow

Each step in our process is separated into its own folder in this repository. The description below describes the order, operations, and output of the scripts in each folder.

- **Alma_Crosswalk** contains the whole collections metadata in a MARC (.mrc) file. The alma_to_csv.py script converts this data to a csv, crosswalking them to the same headers as the data held in the DLXS-version of the colleciton metadata, extracting specific MARC fields or joining fields to make them ready for comparison with the DLXS data in the next step. The crosswalked data is held in alma_full.csv.

- In **DIFF**, our diff.py script compares the two versions of the colleciton metadata held in alma_full.csv and dxls_full.csv. Our script matches collection items on their mms id numbers and then loops through each of the item's fields, flagging any differences beween the two (with some stripping away of formatting differences and whitespace). If differences existed between a field value, those fields were written to the matches.csv document. Additionally, because we expected the Alma metadata to be more robust and up-to-date, we flagged in our matches.csv document any field where the length of the DLXS value was longer for further investigation.

- We work with this matches.csv document further in **Building_CheckLists**. In building_checklists.py, we loop through the matches.csv document ...
