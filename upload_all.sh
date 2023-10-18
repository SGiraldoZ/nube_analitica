#!/bin/bash

# Azure Storage account name
account_name="analyticiscoursera"

# Azure Storage container name
container_name="crudo"

# List of filenames
filenames=("Udemy" "Coursera" "Escuelita_Valores" "Platzi")

# Get the current date in the 'YYYY-MM-DD' format
current_date=$(date +'%Y-%m-%d')

# Iterate over the list of filenames
for filename in "${filenames[*]}"; do
  full_filename="${filename}_${current_date}.*"
  echo "Uploading $full_filename..."
  az storage blob upload \
    --account-name "$account_name" \
    --container-name "$container_name" \
    --name "$full_filename" \
    --file "$full_filename" \
    --auth-mode key
done

echo "Upload completed for all files."
