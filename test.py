from invoicing import invoice

print("--- Starting Invoice System Test ---")

# Run the generation engine
invoice.generate(
    invoices_path="excel_invoices",
    pdfs_path="output_pdfs",
    image_path=None,
    product_id="product_id",
    product_name="product_name",
    amount_purchased="amount-purchased",
    price_per_unit="price_per_unit",
    total_price="total_price"
)

print("--- Engine Execution Finished ---")