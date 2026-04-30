import pandas as pd

file_path = "tmdb_5000_movies.csv"
df = pd.read_csv(file_path)

num_rows = df.shape[0]
num_cols = df.shape[1]
columns = df.columns.tolist()

print("Rows:", num_rows)
print("Columns:", num_cols)
print("Column Names:", columns)

#DATACITE XML GENERATION
from lxml import etree

def generate_datacite_xml(df):
    root = etree.Element("resource",
        xmlns="http://datacite.org/schema/kernel-4"
    )

    # Identifier
    identifier = etree.SubElement(root, "identifier", identifierType="DOI")
    identifier.text = "10.5281/zenodo.tmdb5000anish"

    # Creator
    creators = etree.SubElement(root, "creators")
    creator = etree.SubElement(creators, "creator")
    creator_name = etree.SubElement(creator, "creatorName")
    creator_name.text = "Gaware, Anish"

    # Title
    titles = etree.SubElement(root, "titles")
    title = etree.SubElement(titles, "title")
    title.text = "TMDB 5000 Movies Dataset (Processed Version)"

    # Publisher
    publisher = etree.SubElement(root, "publisher")
    publisher.text = "SRH University Heidelberg"

    # Year
    pub_year = etree.SubElement(root, "publicationYear")
    pub_year.text = "2026"

    # Resource Type
    resource_type = etree.SubElement(root, "resourceType", resourceTypeGeneral="Dataset")
    resource_type.text = "Movie Metadata Dataset"

    # Subjects
    subjects = etree.SubElement(root, "subjects")
    for sub in ["Movies", "Data Mining", "Machine Learning"]:
        subject = etree.SubElement(subjects, "subject")
        subject.text = sub

    # Sizes
    sizes = etree.SubElement(root, "sizes")
    etree.SubElement(sizes, "size").text = f"{df.shape[0]} records"
    etree.SubElement(sizes, "size").text = f"{df.shape[1]} variables"

    # Formats
    formats = etree.SubElement(root, "formats")
    etree.SubElement(formats, "format").text = "text/csv"

    # Description
    descriptions = etree.SubElement(root, "descriptions")
    desc = etree.SubElement(descriptions, "description", descriptionType="Abstract")
    desc.text = f"Dataset containing {df.shape[0]} movies with {df.shape[1]} attributes."

    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")


# Generate XML
xml_output = generate_datacite_xml(df)

# Save file
with open("datacite_metadata.xml", "wb") as f:
    f.write(xml_output)

print("DataCite XML generated!")

#SCHEMA.ORG JSON-LD GENERATION
import json

def generate_schemaorg_json(df):
    schema = {
        "@context": "https://schema.org/",
        "@type": "Dataset",
        "name": "TMDB 5000 Movies Dataset (Processed Version)",
        "description": f"Dataset with {df.shape[0]} movies and {df.shape[1]} features for ML and analysis.",
        "identifier": "https://doi.org/10.5281/zenodo.tmdb5000anish",
        "creator": {
            "@type": "Person",
            "name": "Anish Gaware"
        },
        "publisher": {
            "@type": "Organization",
            "name": "SRH University Heidelberg"
        },
        "datePublished": "2026",
        "inLanguage": "en",
        "keywords": ["movies", "machine learning", "data mining"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "distribution": {
            "@type": "DataDownload",
            "encodingFormat": "text/csv",
            "contentUrl": "https://example.com/download/tmdb_5000_movies.csv"
        },
        "variableMeasured": df.columns.tolist()
    }

    return schema


# Generate JSON
json_output = generate_schemaorg_json(df)

# Save file
with open("schemaorg_metadata.json", "w") as f:
    json.dump(json_output, f, indent=4)

print("schema.org JSON-LD generated!")