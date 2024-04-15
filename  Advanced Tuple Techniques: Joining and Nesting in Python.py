def merge_catalogs(*catalogs):
    merged_catalog = ()
    for catalog in catalogs:
        merged_catalog += catalog
    return merged_catalog

# Example catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Merge catalogs
combined_catalog = merge_catalogs(catalog1, catalog2)

# Display the combined catalog
print("Combined Catalog:")
for product in combined_catalog:
    print(product)