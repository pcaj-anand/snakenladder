import cfg
import random
import sys

def getInputs():
    cfg.snake_tot = int(input("Enter number of snakes: "))
    i = 1
    while(i <= cfg.snake_tot):
        snake_pos = input()
        position_tuple = tuple(int(x) for x in snake_pos.split(" "))
        cfg.snake_pos.append(position_tuple)
        i = i+1
    
    cfg.ladder_tot = int(input("Enter number of ladders: "))
    i = 1
    while(i <= cfg.ladder_tot):
        ladder_pos = input()
        position_tuple = tuple(int(x) for x in ladder_pos.split(" "))
        cfg.ladder_pos.append(position_tuple)
        i = i+1
    
    cfg.players_tot = int(input("Enter number of players: "))
    i = 1
    while(i <= cfg.players_tot):
        name = input()
        cfg.player_names.append(name)
        i = i+1

def displayInputs():
    print(cfg.ladder_pos,cfg.snake_pos,cfg.player_names)

def doMove(playerId):
    cfg.diceValue = random.randint(1,6)
    print(cfg.player_names[playerId], "has rolled a", cfg.diceValue, "and moved from to")

def gameController():   
    getInputs()
    displayInputs()
    if(cfg.players_tot <= 0):
        sys.exit("No one plays with me! :(")
    cfg.current_player_id = 0

    while(cfg.winner == -1):
        doMove(cfg.current_player_id)
        if(cfg.diceValue != 6):
            cfg.current_player_id = cfg.current_player_id + 1
            print(cfg.current_player_id,cfg.players_tot)
            if(cfg.current_player_id > (cfg.players_tot -1)):
                cfg.current_player_id = 0
        if(cfg.diceValue == 6):
            cfg.winner == cfg.current_player_id
            print(cfg.player_names[cfg.current_player_id], "has won.")
            sys.exit(0)
        

gameController()
    
