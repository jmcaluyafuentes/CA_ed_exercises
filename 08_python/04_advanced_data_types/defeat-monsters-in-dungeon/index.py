def defeat_monsters_in_dungeon():
    dungeon = [
        "Goblin", 
        "Gold coins", 
        "Dragon",
        "Dragon",
        "Bandit",
        "Gold coins",
        "Giant Snake"]
    # Your code goes here...
    index = 0
    for monster in dungeon:
        if monster != 'Gold coins':
            dungeon[index] = 'Gold coins'
        index += 1

    return dungeon


