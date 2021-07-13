from checkout import Checkout

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)
