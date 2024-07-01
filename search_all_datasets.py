"""
This script searches and retrieves detailed information for each dataset.
"""

import logging
from api import M2M

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the M2M interface
m2m = M2M()

# Step 1: Print the names of all available datasets
print("Available USGS Datasets:")
with open('dataset_names.txt', 'w') as file:
    for datasetName in m2m.datasetNames:
        print(f"- {datasetName}", file=file)
    

# Step 2: Retrieve and print detailed information for each dataset
print("\nRetrieving detailed information for each dataset...")
datasets = m2m.searchDatasets()

with open('all_dataset_stuff.txt', 'w') as outFyle:
    for dataset in datasets:
        # dataset_name = dataset.get('datasetName')
        # if dataset_name is None:
        #     # print("Dataset Name: Key 'datasetName' not found")
        #     continue  # Skip to the next dataset if 'datasetName' is missing

        # if 'datasetName' not in dataset:
        #     # print("Skipping dataset due to missing 'datasetName' key.")
        #     continue  # Skip to the next dataset

        # dataset_name = dataset['datasetName']
        # print(f"Dataset Name: {dataset_name}")
        # print(f"Description: {dataset.get('description', 'No description available')}")

        # # Safely accessing nested keys in 'temporalCoverage'
        # temporal_coverage = dataset.get('temporalCoverage', {})
        # start_date = temporal_coverage.get('startDate', 'Start date not available')
        # end_date = temporal_coverage.get('endDate', 'End date not available')
        # print(f"Temporal Coverage: {start_date} to {end_date}")

        # print(f"Number of Scenes: {dataset.get('totalScenes', 'Not available')}")
        dataset_name = dataset.get('collectionName')
        if dataset_name is None:
            print("Dataset Name: Key 'datasetName' not found")
            continue  # Skip to the next dataset if 'datasetName' is missing

        if 'collectionName' not in dataset:
            print("Skipping dataset due to missing 'datasetName' key.")
            continue  # Skip to the next dataset

        # dataset_name = dataset['datasetName']
        # print(f"Dataset Name: {dataset_name}")
        print(f"Description: {dataset.get('collectionLongName', 'No description available')}")

        outFyle.write(f"Description: {dataset.get('collectionLongName', 'No description available')}")
        outFyle.write(f"Alias: {dataset.get('datasetAlias', 'No alias available')}\n")
        outFyle.write(f"datasetId: {dataset.get('datasetId', 'No alias available')}\n")
        outFyle.write(f"datasetCategoryName: {dataset.get('datasetCategoryName', 'No alias available')}\n")
        outFyle.write(f"dataOwner: {dataset.get('dataOwner', 'No alias available')}\n")
        outFyle.write(f"dateUpdated: {dataset.get('dateUpdated', 'No alias available')}\n")
        outFyle.write(f"doiNumber: {dataset.get('doiNumber', 'No alias available')}\n")

        # Safely accessing nested keys in 'temporalCoverage'
        temporal_coverage = dataset.get('temporalCoverage', {})
        if temporal_coverage is not None:
            # start_date = temporal_coverage[0]
            # end_date = temporal_coverage[1]
            outFyle.write(f"Temporal Coverage: {temporal_coverage}\n")

        outFyle.write(f"Number of Scenes: {dataset.get('sceneCount', 'Not available')}\n")
        outFyle.write("-" * 50 + "\n")
print("-" * 50)