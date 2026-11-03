from e_object_class.entities.games import Game


g1 = Game("Chess", 2, "Board")
print("Using __str__():", g1)
# Can also access str using str(g1)
print("Using __format__():", f"{g1:file}")
print("Using __repr__():", [g1])
# Can also access repr using repr(g1)