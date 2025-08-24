from src.app.models import Product

def test_product_fields_defaults():
    p = Product(sku="SKU1", name="Arroz", category="abarrotes", price=2.5, stock=10)
    assert p.sku == "SKU1"
    assert p.name == "Arroz"
    assert p.stock == 10
