from checkout import Checkout

def test_CanAddItemPrice():
    co = Checkout()
    co.addItemPrice("a", 1)

def test_canAddItem():
    co = Checkout()
    co.addItem("a")
