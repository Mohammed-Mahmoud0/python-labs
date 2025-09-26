# 4) Product Data Transformer (lambda, map, filter, zip)
#    - Ask user for a list of product names (comma-separated).
#    - Ask user for a list of product prices (comma-separated).
#    - Process them by:
#         - Pairing product with price.
#         - Filtering out items where price <= 0.
#         - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
#    - Save the final result as JSON into "products.json".
#    - Print a preview of the first 5 results.


def product_data_transformation():
    import json

    product_names = list(
        map(str.strip, input("Enter product names (comma-separated): ").split(","))
    )
    product_prices = list(
        map(
            float,
            map(
                str.strip, input("Enter product prices (comma-separated): ").split(",")
            ),
        )
    )

    paired_products = zip(product_names, product_prices)
    filtered_products = filter(lambda x: x[1] > 0, paired_products)
    transformed_products = map(
        lambda x: {"product": x[0], "price": x[1], "discounted": x[1] * 0.9},
        filtered_products,
    )

    final_products = list(transformed_products)

    with open("products.json", "w") as file:
        json.dump(final_products, file, indent=4)

    print("Preview of the first 5 products:")
    for product in final_products[:5]:
        print(product)

