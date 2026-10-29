# lab08/ch08_t07_maintaining_order.py

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

# Find the index of "duck" and store it in duck_index
duck_index = animals.index("duck")

# Insert "cobra" at that index to maintain order
animals.insert(duck_index, "cobra")
