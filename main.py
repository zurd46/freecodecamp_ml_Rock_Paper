from RPS_game import play, quincy, abbey, kris, mrugesh
from RPS import player

# Teste das Spiel mit den verschiedenen Bots
print("Testing against Quincy:")
play(player, quincy, 1000, verbose=True)

print("Testing against Abbey:")
play(player, abbey, 1000, verbose=True)

print("Testing against Kris:")
play(player, kris, 1000, verbose=True)

print("Testing against Mrugesh:")
play(player, mrugesh, 1000, verbose=True)

