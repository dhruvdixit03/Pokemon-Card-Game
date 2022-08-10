#################################################
# TERMPROJECT.py
#
# Your name: Dhruv Dixit
# Your andrew id: dhruvdix
#################################################
import random
import time
import math, os
import decimal
from cmu_112_graphics import *
import pygame
import ast
#################################################
# Pokemon TCG
#################################################
#from CMU 112 website(https://www.cs.cmu.edu/~112/notes/notes-strings.html)
def readFile(path):
    with open('leaderboard.txt', "rt") as f:
        return f.read()

def writeFile(app, path, contents):
    leaderboard = 'leaderboard.txt'
    with open('leaderboard.txt', "wt") as f:
        f.write(contents)
        f.write('\n')

#from CMU 112 website (https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSounds)
class Sound(object):
    def __init__(self, path):
        self.path = path
        self.loops = 1
        pygame.mixer.music.load(path)

    # Returns True if the sound is currently playing
    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    # Loops = number of times to loop the sound.
    # If loops = 1 or 1, play it once.
    # If loops > 1, play it loops + 1 times.
    # If loops = -1, loop forever.
    def start(self, loops=1):
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    # Stops the current sound from playing
    def stop(self):
        pygame.mixer.music.stop()


class Moves(object):
    def __init__(self, name, damage, effect, energycost):
        self.name = name
        self.damage = damage
        self.effect = effect
        self.energycost = energycost
Scratch = Moves('Scratch',10, None, 0)
Ember = Moves('Ember',30, "burn", 1)
Slash = Moves('Slash',30, None, 1)
Flamethrower = Moves('Flamethrower',50, 'burn', 1)
Fire_Spin = Moves('Fire Spin',100, None, 3)
Flare = Moves('Flare',30, None, 1)
Flickering_Flames = Moves('Flickering Flames',70, 'sleep', 2)
Hind_Kick = Moves('Hind Kick',10, None, 0)
Take_Down = Moves('Take Down',80, None, 3)
Fire_Punch = Moves('Fire Punch',30, None, 1)
Smash_Kick = Moves('Smash Kick',20, None, 1)
Flame_Tail = Moves('Flame Tail',30, None, 1)
Rear_Kick = Moves('Rear Kick',30, None, 1)
Fire_Blast = Moves('Fire Blast',70, 'burn', 2)

Tackle = Moves('Tackle',10, None, 0)
Razer_Leaf = Moves('Razer Leaf',30, None, 1)
Toxic_Whip = Moves('Toxic Whip',50, 'poison', 2)
Solarbeam = Moves('Solarbeam',120, None, 4)
Poison_Sting = Moves('Poison Sting',10, 'poison', 0)
Bug_Bite = Moves('Bug Bite',20, None, 1)
Sudden_Sting = Moves('Sudden Sting',10, None, 0)
Sharp_Sting = Moves('Sharp Sting',60, None, 2)
Gnaw = Moves('Gnaw',20, None, 1)
Stun_Spore = Moves('Stun Spore',20, 'paralysis', 1)
Psy_Bolt = Moves('Psy Bolt',30, 'paralysis', 1)
Whirlwind = Moves('Whirlwind',80, None, 3)
Blind = Moves('Blind',20, None, 1)
Poisonpowder = Moves('Poisonpowder',30, 'poison', 1)

Water_Gun = Moves('Water Gun',20, None, 1)
Bite = Moves('Bite',20, None, 1)
Hydro_Tackle = Moves('Hydro Tackle',120, None, 4)
Splash = Moves('Splash',10, None, 0)
Water_Blast = Moves('Water Blast',30, None, 1)
Hyper_Beam = Moves('Hyper Beam',100, None, 3)
Whirlpool = Moves('Whirlpool',100, None, 3)
Double_Slap = Moves('Double Slap',30, 'paralysis', 1)
Wave_Splash = Moves('Wave Splash',60, None, 2)
Dashing_Punch = Moves('Dashing Punch',50, None, 1)
Headbutt = Moves('Headbutt',80, None, 3)
Freezing_Breath = Moves('Freezing Breath',20, 'frozen', 1)
Aurora_Beam = Moves('Aurora Beam',100, None, 3)
Ice_Beam = Moves('Ice Beam',100, 'frozen', 3)
Slap = Moves('Slap',20, None, 1)
Star_Freeze = Moves('Star Freeze',50, 'frozen', 2)

class elementTypes(Moves):
    def __init__(self, name):
        self.name = name
fire = elementTypes('fire')
grass = elementTypes('grass')
water = elementTypes('water')

class Pokemon(Moves):
    def __init__(self, name, HP, moves, elementtype, img):
        self.name = name
        self.HP = HP
        self.moves = moves #at most 2 moves
        self.elementtype = elementtype #fire, water, or grass
        self.img = img
    
    def __repr__(self):
        return f'{self.name}'
        
    def strengthsAndWeaknesses(self,other,type,HP):           
        #fire scenarios
        if self.elementtype == fire and other.elementtype == water:
            self.HP = HP//1.5
        if self.elementtype == fire and other.elementtype == grass:
            other.HP = HP//1.5
        
        #water scenarios
        if self.elementtype == water and other.elementtype == fire:
            other.HP = HP//1.5
        if self.elementtype == water and other.elementtype == grass:
            self.HP = HP//1.5

        #grass scenarios
        if self.elementtype == grass and other.elementtype == fire:
            self.HP = HP//1.5

        if self.elementtype == grass and other.elementtype == water:
            other.HP = HP//1.5

#fire pokemon
Charmander = Pokemon('Charmander', 50,[Scratch, Ember], fire, 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Charmeleon = Pokemon('Charmeleon', 80,[Slash, Flamethrower], fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Charizard = Pokemon('Charizard', 120,[Fire_Spin],fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Vulpix = Pokemon('Vulpix', 70,[Flare],  fire,'Vulpix.png')
Ninetales = Pokemon('Ninetales', 90,[Flickering_Flames],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Growlithe = Pokemon('Growlithe', 70,[Hind_Kick, Flare],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Arcanine = Pokemon('Arcanine', 100,[Flamethrower, Take_Down],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Magmar = Pokemon('Magmar', 80,[Fire_Punch, Flamethrower],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Ponyta = Pokemon('Ponyta', 40,[Smash_Kick, Flame_Tail],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Rapidash = Pokemon('Rapidash', 90,[Rear_Kick, Fire_Blast],  fire,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')

#grass pokemon
Bulbasaur = Pokemon('Bulbasaur', 60,[Tackle, Razer_Leaf],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Ivysaur = Pokemon('Ivysaur', 100,[Razer_Leaf, Toxic_Whip],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Venusaur = Pokemon('Venusaur', 100,[Solarbeam],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Weedle = Pokemon('Weedle', 40,[Poison_Sting],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Kakuna = Pokemon('Kakuna', 80,[Bug_Bite],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Beedrill = Pokemon('Beedrill', 120,[Sudden_Sting, Sharp_Sting],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Caterpie = Pokemon('Caterpie', 50,[Gnaw],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Metapod = Pokemon('Metapod', 70,[Stun_Spore],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Butterfree = Pokemon('Butterfree', 130,[Psy_Bolt, Whirlwind],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Tangela = Pokemon('Tangela', 50,[Blind, Poisonpowder],  grass,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')

#water pokemon
Squirtle = Pokemon('Squirtle', 50,[Water_Gun],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Wartortle = Pokemon('Wartortle', 70,[Bite],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Blastoise = Pokemon('Blastoise', 160,[Hydro_Tackle],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Magikarp = Pokemon('Magikarp', 30,[Splash],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Gyarados = Pokemon('Gyarados', 120,[Water_Blast, Hyper_Beam],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Poliwag = Pokemon('Poliwag', 60,[Water_Gun],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Poliwhirl = Pokemon('Poliwhirl', 90,[Double_Slap, Wave_Splash],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Poliwrath = Pokemon('Poliwrath', 140,[Dashing_Punch, Whirlpool],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Seel = Pokemon('Seel', 80,[Headbutt],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Dewgong = Pokemon('Dewgong', 120,[Freezing_Breath, Aurora_Beam],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Lapras = Pokemon('Lapras', 120,[Ice_Beam],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Staryu = Pokemon('Staryu', 40,[Slap],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')
Starmie = Pokemon('Starmie', 60,[Star_Freeze],  water,'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg')

class Player(object):
    def __init__(self, bench, prizecards, battlefield):
        self.bench = bench
        self.battlefield = battlefield
        self.prizecards = prizecards
         
    def playerAttack(self, other, battlefield, attack, HP, elementtype):
        other.battlefield.HP -= attack
      
###############
#GAME OVER
###############
#ending screen
def gameOverMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    if len(app.bench) == 0 or len(app.prizecards) == 0:
        canvas.create_text(500,293.5,text = 'YOU LOST' , font = 'Arial 48 bold')
    elif len(app.opponentbench) == 0 or len(app.opponentprizecards) == 0:
        canvas.create_text(500,293.5,text = 'YOU WON' , font = 'Arial 48 bold')

##################
# Death mode
##################
#choosing new pokemon after death
def deathMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    if len(app.bench) == 0 or len(app.prizecards) == 0:
        canvas.create_text(500,293.5,text = 'YOU LOST' , font = 'Arial 48 bold')
    elif len(app.opponentbench) == 0 or len(app.opponentprizecards) == 0:
        canvas.create_text(500,293.5,text = 'YOU WON' , font = 'Arial 48 bold')
    else:
        canvas.create_text(500,50,text = 'Which card from your bench do you want to place on the battlefield?' , font = 'Arial 24 bold')
        x = 500
        y = 150
        for pokemon in app.bench:
            canvas.create_rectangle(x-75,y-25,x+75,y+25,width = 3, fill = "light blue")
            canvas.create_text(x,y,text = pokemon.name, font = 'Arial 18 bold', fill = 'dark blue')
            y += 60 
def deathMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    x = 500
    y = 150
    for pokemon in app.bench:
        if x-75 <= app.cx <= x+75 and y-25 <= app.cy <= y+25:
            app.battlefield.append(pokemon)
            app.bench.remove(pokemon)
            app.mode = 'drawCardMode'
        y += 60
#summarizes opponent move
def opponentMoveSummaryMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50,text = 'OPPONENT MOVE SUMMARY' , font = 'Arial 24 bold')
    canvas.create_text(500,150,text = f'OPPONENT CHOSE : {app.opponentbattlefield[0]}' , font = 'Arial 18 bold')
    canvas.create_text(500,250,text = f'OPPONENT DID : {app.opponentattackdamage} DAMAGE' , font = 'Arial 18 bold')
    if len(app.battlefield)>0:
        canvas.create_image(250, 270, image=ImageTk.PhotoImage(app.opponentbattlefield[0].img))
        canvas.create_image(750, 270, image=ImageTk.PhotoImage(app.battlefield[0].img))
        canvas.create_text(500,350,text = f'YOUR POKEMON ({app.battlefield[0]}) HAS {app.battlefield[0].HP}HP LEFT' , font = 'Arial 18 bold')
    else:
        canvas.create_image(250, 270, image=ImageTk.PhotoImage(app.opponentbattlefield[0].img))
        canvas.create_text(500,350,text = f'YOUR POKEMON HAS FAINTED' , font = 'Arial 18 bold')

def opponentMoveSummaryMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if len(app.battlefield) == 0:
        app.mode = 'deathMode'
    else:
        app.mode = 'drawCardMode'

##########################
# move select hard mode
##########################
#dictionary with key as damage and value as pokemon
#list with sorted damage values
def opponentMoveSelectHardMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,293.5,text = 'OPPONENT IS THINKING...', font = 'Arial 28 bold', fill = 'dark blue')
    canvas.create_text(500,50,text = 'click to see damage!', font = 'Arial 24 bold', fill = 'dark blue')
def opponentMoveSelectHardMode_mousePressed(app,event):
    #MONTE CARLOOOO
    #inspiration from https://www.cs.cmu.edu/~112/notes/notes-monte-carlo.html
    simulations = 500
    #numerical adding dictionaries
    pokedamage = dict()
    pokedamagetaken = dict()
    pokemonranks = dict()
    
    #regular equals dictionaries
    damagekey = dict()
    damageranks = dict()
    pokechances = dict()

    for poke in app.opponentbench:
        app.opponentpokemons.append(poke)
    app.opponentpokemons.append(app.opponentbattlefield[0])
    
    #set adding dictionaries to initialize at 0
    for pokemon in app.opponentpokemons:
        pokemonranks[pokemon] = 0
    app.opponentpokemons = []
    
    #create list of all my pokemon
    for poke in app.bench:
        app.playerpokemons.append(poke)
    app.playerpokemons.append(app.battlefield[0])

    #start simulation
    for sims in range(simulations):
        totalranks = 0 
        app.opponentpokemons = []
        #update opponentpokemonlist every simulation
        for poke in app.opponentbench:
            app.opponentpokemons.append(poke)
        app.opponentpokemons.append(app.opponentbattlefield[0])
        #loop through all of opponents pokemon
        for otherpokemon in app.opponentpokemons:
            pokedamage[otherpokemon] = 0
            pokedamagetaken[otherpokemon] = 0
            damagevals = []
            choices = []
            mypokemon = random.choice(app.playerpokemons)
            for viablemoves in otherpokemon.moves:
                #if viablemoves.energycost <= app.opponentenergy:
                choices.append(viablemoves)
            #randomly select opponent and player attack
            opponentattack = random.choice(choices).damage
            playerattack = random.choice(mypokemon.moves).damage
            #damage adjustments for type difference
            if mypokemon.elementtype == fire and otherpokemon.elementtype == grass or mypokemon.elementtype == grass and otherpokemon.elementtype == water or mypokemon.elementtype == water and otherpokemon.elementtype == fire:
                opponentattack = opponentattack // 1.5
            if mypokemon.elementtype == grass and otherpokemon.elementtype == fire or mypokemon.elementtype == water and otherpokemon.elementtype == grass or mypokemon.elementtype == fire and otherpokemon.elementtype == water:
                opponentattack = opponentattack * 1.5
            #sets damage done and damage taken by pokemon in a dictionary
            pokedamage[otherpokemon] = opponentattack
            pokedamagetaken[otherpokemon] = playerattack
        #adding stats to dictionairies to eventually get percentage chance of choosing pokemon      
        for pokemon in app.opponentpokemons: 
            damagekey[pokedamage[pokemon]] = pokemon
        for key in pokedamage:
            damagevals.append(pokedamage[key])
            damagevals.sort()
        for vals in damagevals:
            damageranks[vals] = len(damagevals) - damagevals.index(vals)
        for pokemon in app.opponentpokemons:
            pokemonranks[pokemon] += damageranks[pokedamage[pokemon]]
        damagekey = dict()
        damageranks = dict()
        damagevals = []    
    #calculation for percent chance
    for pokemon in app.opponentpokemons:     
        n = 0
        for index in range(len(app.opponentpokemons)):
            n += (index + 1)
        pokechances[pokemon] = (((simulations*(len(app.opponentpokemons)+1))-pokemonranks[pokemon]) / (simulations*n))
    #creating lists with pokemon chances
    pokechooselist = []
    pokeints = []
    for key in pokechances:
        pokeints.append(int(pokechances[key]*100))
    for pokenum in range(len(app.opponentpokemons)):
        for percentnum in range(pokeints[pokenum]):
            pokechooselist.append(app.opponentpokemons[pokenum])
    #attack and switch battlefield
    fighter = random.choice(pokechooselist)
    opponent1 = Player([], 6, fighter)
    player1 = Player([], 6, app.battlefield[0])
    if app.opponentbattlefield[0] == fighter:
        if len(fighter.moves) == 1:
            opponentattack = fighter.moves[0].damage
            app.opponentattackdamage = opponentattack
        else:
            opponentattack = fighter.moves[1].damage
            app.opponentattackdamage = opponentattack
        opponent1.playerAttack(player1,opponent1.battlefield, opponentattack, opponent1.battlefield.HP, opponent1.battlefield.elementtype)
        if app.battlefield[0].HP <= 0:
            app.battlefield.pop()
            app.prizecards.pop()
            if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
                myData1 = ast.literal_eval(readFile('leaderboard.txt'))
                for key in myData1:
                    if app.turns < myData1[key]:
                        writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
                app.mode = 'gameOverMode'
            else:
                app.mode = 'deathMode'
    else:
        app.opponentbattlefield.append(fighter)
        app.opponentbench.append(app.opponentbattlefield[0])
        app.opponentbattlefield.pop(0)
        app.opponentbench.remove(fighter)
        if len(fighter.moves) == 1:
            opponentattack = fighter.moves[0].damage
            app.opponentattackdamage = opponentattack
        else:
            opponentattack = fighter.moves[1].damage
            app.opponentattackdamage = opponentattack
        opponent1.playerAttack(player1,opponent1.battlefield, opponentattack, opponent1.battlefield.HP, opponent1.battlefield.elementtype)
        if app.battlefield[0].HP <= 0:
            app.battlefield.pop()
            app.prizecards.pop()
            if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
                myData1 = ast.literal_eval(readFile('leaderboard.txt'))
                for key in myData1:
                    if app.turns < myData1[key]:
                        writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
                app.mode = 'gameOverMode'
            else:
                app.mode = 'deathMode'
    if len(app.opponentpotions)>0:
        if fighter.HP <= 30:
            potion = random.choice(app.opponentpotions)
            if potion == 'heal':
                fighter.HP += 20
                app.opponentpotions.remove('heal')
            if potion == 'hyper potion':
                fighter.HP += 100
                app.opponentpotions.remove('hyper potion')
            if potion == 'revive':
                if len(app.opponentbench) < 5: 
                    app.opponentbench.append(random.choice(app.opponentpokemonlist))
                    app.mopponentpokemonlist.remove(app.opponentbench[len(app.opponentbench)-1])
                app.opponentpotions.remove('revive')
            app.mode = 'opponentPotionSummaryMode'
            return
    pokedamage = dict()
    pokedamagetaken = dict()
    damagekey = dict()
    damageranks = dict()
    pokechances = dict()
    damagevals = []
    app.mode = 'opponentMoveSummaryMode'

#########################
#opponent potion summary
#########################
def opponentPotionSummaryMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,293.5,text = f'Opponent {app.opponentbattlefield[0]} used a potion!', font = 'Arial 28 bold', fill = 'dark blue')
    canvas.create_text(500,50,text = 'click to continue...', font = 'Arial 24 bold', fill = 'dark blue')
def opponentPotionSummaryMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'opponentMoveSummaryMode'


##########################
# player insufficient energy mode
##########################
def playerInsufficientEnergyMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,293.5,text = f'{app.battlefield[0]} missed!(not enough energy...)', font = 'Arial 28 bold', fill = 'dark blue')
    canvas.create_text(500,50,text = 'click to choose another pokemon', font = 'Arial 24 bold', fill = 'dark blue')
def playerInsufficientEnergyMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if app.difficulty == 'easy':
        app.mode = 'opponentMoveSelectEasyMode'
    else:
        app.mode = 'opponentMoveSelectHardMode'
##########################
# opponent insufficient energy mode
##########################
def opponentInsufficientEnergyMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,293.5,text = f'Opponents {app.opponentbattlefield[0]} missed!(not enough energy...)', font = 'Arial 28 bold', fill = 'dark blue')
    canvas.create_text(500,50,text = 'Opponent skips turn', font = 'Arial 24 bold', fill = 'dark blue')
def opponentInsufficientEnergyMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'drawCardMode'


##########################
# opponent move select easy mode
##########################
def opponentMoveSelectEasyMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,293.5,text = 'OPPONENT IS THINKING...', font = 'Arial 28 bold', fill = 'dark blue')
    canvas.create_text(500,50,text = 'click to see damage!', font = 'Arial 24 bold', fill = 'dark blue')
def opponentMoveSelectEasyMode_mousePressed(app,event):
    app.opponentenergy += 1
    opponentmove = random.choice(app.opponentbattlefield[0].moves)
    if opponentmove.energycost > app.opponentenergy:
        app.mode = 'opponentInsufficientEnergyMode'
        return
    opponentattack = opponentmove.damage
    app.opponentenergy -= opponentmove.energycost
    if app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == water or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == fire:
        opponentattack = opponentattack // 1.5
    if app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == fire or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == water:
        opponentattack = opponentattack * 1.5
    app.opponentattackdamage = opponentattack
    opponent1 = Player([], 6, app.opponentbattlefield[0])
    player1 = Player([], 6, app.battlefield[0])
    opponent1.playerAttack(player1,opponent1.battlefield, opponentattack, opponent1.battlefield.HP, opponent1.battlefield.elementtype)
    if app.battlefield[0].HP <= 0:
        app.battlefield.pop()
        app.prizecards.pop()
        if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
            myData1 = ast.literal_eval(readFile('leaderboard.txt'))
            for key in myData1:
                if app.turns < myData1[key]:
                    writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
            app.mode = 'gameOverMode'
            return
    app.mode = 'opponentMoveSummaryMode'

#####################
#player move summary
#####################
def playerMoveSummaryMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50,text = 'PLAYER MOVE SUMMARY' , font = 'Arial 24 bold')
    canvas.create_text(500,150,text = f'YOU CHOSE : {app.battlefield[0]}' , font = 'Arial 18 bold')
    canvas.create_text(500,250,text = f'YOU DID : {app.playerattackdamage} DAMAGE' , font = 'Arial 18 bold')
    if len(app.opponentbattlefield)>0:
        canvas.create_image(750, 270, image=ImageTk.PhotoImage(app.opponentbattlefield[0].img))
        canvas.create_image(250, 270, image=ImageTk.PhotoImage(app.battlefield[0].img))
        canvas.create_text(500,350,text = f'OPPONENT POKEMON ({app.opponentbattlefield[0]}) HAS {app.opponentbattlefield[0].HP}HP LEFT' , font = 'Arial 18 bold')
    else:
        canvas.create_image(250, 270, image=ImageTk.PhotoImage(app.battlefield[0].img))
        canvas.create_text(500,350,text = f'OPPONENT POKEMON HAS FAINTED' , font = 'Arial 18 bold')
    canvas.create_text(500,500,text = f'click screen to continue...' , font = 'Arial 12 bold')

def playerMoveSummaryMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if len(app.opponentbattlefield) == 0:
        app.mode = 'drawCardMode'
    else:
        if app.difficulty == 'easy':
            app.mode = 'opponentMoveSelectEasyMode'
        else:
            app.mode = 'opponentMoveSelectHardMode'
    

###################
#move select mode
###################
def playerMoveSelectMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    x = 500
    y = 150
    canvas.create_text(500,50,text = 'SELECT A MOVE', font = 'Arial 28 bold', fill = 'dark blue')
    for move in app.battlefield[0].moves:
        canvas.create_rectangle(x-75,y-25,x+75,y+25,width = 3, fill = "light blue")
        canvas.create_text(x,y,text = f'{move.name}, {move.energycost}', font = 'Arial 18 bold', fill = 'dark blue')
        y += 60 
def playerMoveSelectMode_mousePressed(app,event):
    #check type matchup for damage output
    app.cx = event.x
    app.cy = event.y
    app.turns += 1
    print(app.turns)
    if len(app.battlefield[0].moves) > 1:
        #MOVE 1
        if 425 <= app.cx <= 575 and 125 <= app.cy <= 175: 
            #app.click.start()
            myattackname = app.battlefield[0].moves[0]
            myattack = app.battlefield[0].moves[0].damage
            if app.energy < myattackname.energycost:
                app.mode = 'playerInsufficientEnergyMode'
                return
            app.energy -= myattackname.energycost
            if app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == water or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == fire:
                myattack = myattack * 1.5
            if app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == fire or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == water:
                myattack = myattack // 1.5 
            app.playerattackdamage = myattack     
            player1 = Player([], 6, app.battlefield[0])
            opponent1 = Player([], 6, app.opponentbattlefield[0])
            player1.playerAttack(opponent1, player1.battlefield, myattack, player1.battlefield.HP, player1.battlefield.elementtype)

            if app.opponentbattlefield[0].HP <= 0:
                app.opponentbattlefield.pop()
                app.opponentprizecards.pop()
                if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
                    myData1 = ast.literal_eval(readFile('leaderboard.txt'))
                    for key in myData1:
                        if app.turns < myData1[key]:
                            writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
                    app.mode = 'gameOverMode'
                    return
            
            app.mode = 'playerMoveSummaryMode'
        
        #MOVE 2
        if 425 <= app.cx <= 575 and 185 <= app.cy <= 235:
            #app.click.start()
            myattackname = app.battlefield[0].moves[1]
            myattack = app.battlefield[0].moves[1].damage
            if app.energy < myattackname.energycost:
                app.mode = 'playerInsufficientEnergyMode'
                return
            app.energy -= myattackname.energycost
            if app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == water or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == fire:
                myattack = myattack * 1.5
            if app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == fire or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == water:
                myattack = myattack // 1.5 
            app.playerattackdamage = myattack     
            player1 = Player([], 6, app.battlefield[0])
            opponent1 = Player([], 6, app.opponentbattlefield[0])
            player1.playerAttack(opponent1, player1.battlefield, myattack, player1.battlefield.HP, player1.battlefield.elementtype)

            if app.opponentbattlefield[0].HP <= 0:
                app.opponentbattlefield.pop()
                app.opponentprizecards.pop()
                if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
                    myData1 = ast.literal_eval(readFile('leaderboard.txt'))
                    for key in myData1:
                        if app.turns < myData1[key]:
                            writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
                    app.mode = 'gameOverMode'
                    return
            
            app.mode = 'playerMoveSummaryMode'
              
    if len(app.battlefield[0].moves) == 1:
        if 425 <= app.cx <= 575 and 125 <= app.cy <= 175 or 185 <= app.cy <= 235:
            #app.click.start()
            myattackname = app.battlefield[0].moves[0]
            myattack = app.battlefield[0].moves[0].damage
            if app.energy < myattackname.energycost:
                app.mode = 'playerInsufficientEnergyMode'
                return
            app.energy -= myattackname.energycost
            if app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == water or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == fire:
                myattack = myattack * 1.5
            if app.battlefield[0].elementtype == grass and app.opponentbattlefield[0].elementtype == fire or app.battlefield[0].elementtype == water and app.opponentbattlefield[0].elementtype == grass or app.battlefield[0].elementtype == fire and app.opponentbattlefield[0].elementtype == water:
                myattack = myattack // 1.5    
            app.playerattackdamage = myattack  
            player1 = Player([], 6, app.battlefield[0])
            opponent1 = Player([], 6, app.opponentbattlefield[0])
            player1.playerAttack(opponent1, player1.battlefield, myattack, player1.battlefield.HP, player1.battlefield.elementtype)
            if app.opponentbattlefield[0].HP <= 0:
                app.opponentbattlefield.pop()
                app.opponentprizecards.pop()
                if len(app.prizecards) == 0 or len(app.opponentprizecards) == 0:
                    myData1 = ast.literal_eval(readFile('leaderboard.txt'))
                    for key in myData1:
                        if app.turns < myData1[key]:
                            writeFile(app, 'leaderboard.txt', repr({app.username: app.turns}))
                    app.mode = 'gameOverMode'
                    return
            app.mode = 'playerMoveSummaryMode'
    

    

#################
#switch pokemon with bench
#################
def benchMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50,text = 'Which benched pokemon do you want to place on your battlefield?' , font = 'Arial 24 bold')
    x = 500
    y = 150
    for pokemon in app.bench:
        canvas.create_rectangle(x-75,y-25,x+75,y+25,width = 3, fill = "light blue")
        canvas.create_text(x,y,text = pokemon.name, font = 'Arial 18 bold', fill = 'dark blue')
        y += 60
    canvas.create_rectangle(920,517,980,557, width = 3, fill = "light blue")
    canvas.create_text(950,537,text = "BACK", font = 'Arial 12 bold')
def benchMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if 920 <= app.cx <= 980 and 517 <= app.cy <= 557:
        #app.click.start()
        app.mode = 'battleMode'
        return
    if 425 <= app.cx <= 575 and 125 <= app.cy <= 175:
        #app.click.start()
        app.battlefield.append(app.bench[0])
        app.bench.append(app.battlefield[0])
        app.battlefield.pop(0)
        app.bench.pop(0)
        app.mode = 'battleMode'
    if 425 <= app.cx <= 575 and 185 <= app.cy <= 235:
        #app.click.start()
        app.battlefield.append(app.bench[1])
        app.bench.append(app.battlefield[0])
        app.battlefield.pop(0)
        app.bench.pop(1)
        app.mode = 'battleMode'
    if 425 <= app.cx <= 575 and 245 <= app.cy <= 295:
        #app.click.start()
        app.battlefield.append(app.bench[2])
        app.bench.append(app.battlefield[0])
        app.battlefield.pop(0)
        app.bench.pop(2)
        app.mode = 'battleMode'
    if 425 <= app.cx <= 575 and 305 <= app.cy <= 355:
        #app.click.start()
        app.battlefield.append(app.bench[3])
        app.bench.append(app.battlefield[0])
        app.battlefield.pop(0)
        app.bench.pop(3)
        app.mode = 'battleMode'
    if 425 <= app.cx <= 575 and 365 <= app.cy <= 415:
        #app.click.start()
        app.battlefield.append(app.bench[4])
        app.bench.append(app.battlefield[0])
        app.battlefield.pop(0)
        app.bench.pop(4)
        app.mode = 'battleMode'
        
    
#############
#potion mode
#############
def potionMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50,text = 'Which potion do you want to use on your battlefield pokemon?' , font = 'Arial 24 bold')
    x = 500
    y = 150
    for potion in app.potions:
        canvas.create_rectangle(x-75,y-25,x+75,y+25,width = 3, fill = "violet")
        canvas.create_text(x,y,text = potion, font = 'Arial 18 bold', fill = 'dark blue')
        y += 60
    canvas.create_text(x,325,text = 'heal: heals your battlefield pokemon for 20 HP', font = 'Arial 18 bold', fill = 'dark blue')
    canvas.create_text(x,350,text = 'hyper potion: heals your battlefield pokemon for 100 HP', font = 'Arial 18 bold', fill = 'dark blue')
    canvas.create_text(x,375,text = 'revive: adds a random pokemon from your pokemon list to your bench', font = 'Arial 18 bold', fill = 'dark blue')
    canvas.create_rectangle(920,517,980,557, width = 3, fill = "light blue")
    canvas.create_text(950,537,text = "BACK", font = 'Arial 12 bold')

def potionMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if 920 <= app.cx <= 980 and 517 <= app.cy <= 557:
        app.mode = 'battleMode'
        return
    if 425 <= app.cx <= 575 and 125 <= app.cy <= 175:
        #app.click.start()
        if app.potions[0] == 'heal':
            app.battlefield[0].HP += 20
            app.potions.remove(app.potions[0])
            app.mode = 'battleMode'
            return
        if app.potions[0] == 'hyper potion':
            app.battlefield[0].HP += 100
            app.potions.remove(app.potions[0])
            app.mode = 'battleMode'
            return
        if app.potions[0] == 'revive':
            if len(app.bench) < 5: 
                app.bench.append(random.choice(app.mypokemonlist))
                app.mypokemonlist.remove(app.bench[len(app.bench)-1])
            app.potions.remove(app.potions[0])
            app.mode = 'battleMode'
            return
    if 425 <= app.cx <= 575 and 185 <= app.cy <= 235:
        #app.click.start()
        if app.potions[1] == 'heal':
            app.battlefield[0].HP += 20
            app.potions.remove(app.potions[1])
            app.mode = 'battleMode'
            return
        if app.potions[1] == 'hyper potion':
            app.battlefield[0].HP += 100
            app.potions.remove(app.potions[1])
            app.mode = 'battleMode'
            return
        if app.potions[1] == 'revive':
            if len(app.bench) < 5: 
                app.bench.append(random.choice(app.mypokemonlist))
                app.mypokemonlist.remove(app.bench[len(app.bench)-1])
            app.potions.remove(app.potions[1])
            app.mode = 'battleMode'
            return
        
    if 425 <= app.cx <= 575 and 245 <= app.cy <= 295:
        #app.click.start()
        if app.potions[2] == 'heal':
            app.battlefield[0].HP += 20
            app.potions.remove(app.potions[2])
            app.mode = 'battleMode'
            return
        if app.potions[2] == 'hyper potion':
            app.battlefield[0].HP += 100
            app.potions.remove(app.potions[2])
            app.mode = 'battleMode'
            return
        if app.potions[2] == 'revive':
            if len(app.bench) < 5: 
                app.bench.append(random.choice(app.mypokemonlist))
                app.mypokemonlist.remove(app.bench[len(app.bench)-1])
            app.potions.remove(app.potions[2])
            app.mode = 'battleMode'
            return
        



###############
#BATTLE MODE
###############
def battleMode_redrawAll(app,canvas): 
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(820,380,text = f'BATTLEFIELD : {app.battlefield[0]}({app.battlefield[0].HP}HP)', font = 'Arial 18 bold')
    canvas.create_text(820,430,text = f'BENCH : {app.bench}', font = 'Arial 12 bold')
    canvas.create_text(820,520,text = f'YOUR PRIZECARDS : {len(app.prizecards)}', font = 'Arial 12 bold')
    canvas.create_text(820,540,text = f'OPPONENT PRIZECARDS : {len(app.opponentprizecards)}', font = 'Arial 12 bold')
    canvas.create_text(820,480,text = f'ENERGY : {app.energy}', font = 'Arial 12 bold')

    drawAttackButton(app, canvas)
    drawBenchPokemon(app,canvas)
    drawPotionButton(app,canvas)
    drawBoard(app,canvas)
    canvas.create_text(820,30,text = "What do you want to do?", font = 'Arial 28 bold')
def drawAttackButton(app, canvas):
    canvas.create_rectangle(650,100,990,160, width = 3, fill = "red")
    canvas.create_text(820,130,text = "ATTACK", font = 'Arial 22 bold') 
def drawBenchPokemon(app,canvas):
    canvas.create_rectangle(650,200,990,260, width = 3, fill = "light blue")
    canvas.create_text(820,230,text = "PLACE POKEMON ON BENCH", font = 'Arial 22 bold')
def drawPotionButton(app,canvas):
    canvas.create_rectangle(650,300,990,360, width = 3, fill = "violet")
    canvas.create_text(820,330,text = "POTIONS", font = 'Arial 22 bold')
    

def drawBoard(app, canvas):
    #import board
    canvas.create_image(320, 293.5, image=ImageTk.PhotoImage(app.playingmat))
    #make my deck
    canvas.create_image(588, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(590, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(592, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(594, 388, image=ImageTk.PhotoImage(app.pokemoncard))

    #make opponent deck
    canvas.create_image(52, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(54, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(56, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(58, 199, image=ImageTk.PhotoImage(app.pokemoncard))

    #my prize cards
    y = 525
    for card in range(0,len(app.prizecards)//2):
        canvas.create_image(50, y, image=ImageTk.PhotoImage(app.pokemoncard))
        y -= 100
    y = 518
    for card in range(len(app.prizecards)//2, len(app.prizecards)):
        canvas.create_image(65, y, image=ImageTk.PhotoImage(app.pokemoncard))
        y -= 100

    #opponent prize cards
    y = 262
    for card in range(0,len(app.opponentprizecards)//2):
        canvas.create_image(590, y, image=ImageTk.PhotoImage(app.pokemoncard))
        y -= 100
    y = 269
    for card in range(len(app.opponentprizecards)//2, len(app.opponentprizecards)):
        canvas.create_image(575, y, image=ImageTk.PhotoImage(app.pokemoncard))
        y -= 100

    if len(app.battlefield) > 0:
        canvas.create_text(160, 250, text = f'{app.battlefield[0].HP}HP', fill = 'green', font = 'Arial 24 bold')
        canvas.create_image(160, 320, image=ImageTk.PhotoImage(app.battlefield[0].img))
    if len(app.opponentbattlefield) > 0:
        canvas.create_text(480, 337, text = f'{app.opponentbattlefield[0].HP}HP', fill = 'red', font = 'Arial 24 bold')
        canvas.create_image(480, 267, image=ImageTk.PhotoImage(app.opponentbattlefield[0].img))

    x = 157
    y = 520
    oppx = 483
    oppy = 67
    for pokemon in app.bench:
        canvas.create_image(x, y, image=ImageTk.PhotoImage(pokemon.img))
        canvas.create_text(x, 450, text = f'{pokemon.HP}HP', fill = 'gray', font = 'Arial 24 bold')
        x += 82
    for pokemon in app.opponentbench:
        canvas.create_image(oppx, oppy, image=ImageTk.PhotoImage(app.pokemoncard))
        oppx -= 82
    #battlefield
    #canvas.create_image(500, 293.5, image=ImageTk.PhotoImage(app.battlefieldpokemon))

def battleMode_mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    #attack box click
    if 650<= app.cx <=990 and 100<= app.cy <=160:
        #app.click.start()
        app.mode = 'playerMoveSelectMode'
    #bench pokemon click  
    if 650<=app.cx<=990 and 200<=app.cy<=260:
        #app.click.start()
        app.mode = 'benchMode'
    if 650<=app.cx<=990 and 300<=app.cy<=360:
        #app.click.start()
        app.mode = 'potionMode'

################
# powerups
################
def playerHpBoostMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,100, text = 'YOUR pokemon recieved a powerup!', font = 'Arial 30 bold')
    canvas.create_text(500,293.5,text = f'YOUR {app.bench[len(app.bench)-1]} HP has increased by 33%', font = 'Arial 24 bold') 
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def playerHpBoostMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'opponentDrawCardMode'

def playerDamageBoostMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,100, text = 'YOUR pokemon recieved a powerup!', font = 'Arial 30 bold')
    canvas.create_text(500,293.5,text = f'YOUR {app.bench[len(app.bench)-1]} damage has increased by 33%', font = 'Arial 24 bold') 
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def playerDamageBoostMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'opponentDrawCardMode'

def opponentHpBoostMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR opponents pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,100, text = 'YOUR opponents pokemon recieved a powerup!', font = 'Arial 30 bold')
    canvas.create_text(500,293.5,text = 'OPPONENTS pokemon HP has increased by 33%', font = 'Arial 24 bold') 
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def opponentHpBoostMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'battleMode'

def opponentDamageBoostMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR opponents pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,100, text = 'YOUR opponents pokemon recieved a powerup!', font = 'Arial 30 bold')
    canvas.create_text(500,293.5,text = 'OPPONENTS pokemon damage has increased by 33%', font = 'Arial 24 bold') 
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def opponentDamageBoostMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'battleMode'

def playerEnergyBoostMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,100, text = 'YOU recieved a powerup!', font = 'Arial 30 bold')
    canvas.create_text(500,293.5,text = f'YOUR Energy has increased by 1!', font = 'Arial 24 bold') 
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def playerEnergyBoostMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'opponentDrawCardMode'

def playerPotionMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'YOUR pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,200, text = 'YOU recieved a potion!', font = 'Arial 30 bold')
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def playerPotionMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'opponentDrawCardMode'

def opponentPotionMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50, text = 'Opponent pokemon came with a surprise...', font = 'Arial 30 bold')
    canvas.create_text(500,200, text = 'Opponent recieved a potion!', font = 'Arial 30 bold')
    canvas.create_text(500,550, text = 'click to continue...', font = 'Arial 12 bold')
def opponentPotionMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'battleMode'



################
#Draw card mode
################
def drawCardMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(760,380,text = "<------ CLICK DECK TO DRAW CARD", font = 'Arial 12 bold')  
    drawBoard(app,canvas)
def drawCardMode_mousePressed(app,event): 
    #draws card by clicking on deck 
    app.energy += 1
    app.cx = event.x
    app.cy = event.y
    #if opponent battlefield is empty, it will automatically place a card onto its battlefield
    if len(app.opponentbattlefield) == 0 and len(app.opponentbench) > 0:
        app.opponentbattlefield.append(random.choice(app.opponentbench))
        app.opponentbench.remove(app.opponentbattlefield[0])
    #card drawing for player and opponent
    if 550 <= app.cx <= 625 and 338 <= app.cy <= 438:
        #app.click.start()
        #revive
        #if on last prizecard choose pokemon from deck
        if len(app.bench) <5:
            app.bench.append(random.choice(app.mypokemonlist))
            app.mypokemonlist.remove(app.bench[len(app.bench)-1])
            #MAX HP BOOST POWERUP
            if random.randint(1,7) == 1:
                app.bench[len(app.bench)-1].HP = int((app.bench[len(app.bench)-1].HP)*1.33)
                app.mode = 'playerHpBoostMode'
                return
            #attackboost
            if random.randint(1,7) == 1:
                for moves in app.bench[len(app.bench)-1].moves:
                    moves.damage = int((moves.damage)*1.33)
                app.mode = 'playerDamageBoostMode'
                return
            #potions
            if random.randint(1,6) == 1:
                app.potions.append('heal')
                app.mode = 'playerPotionMode'
                return
            if random.randint(1,5) == 1:
                app.potions.append('hyper potion')
                app.mode = 'playerPotionMode'
                return
            if random.randint(1,4) == 1:
                app.potions.append('revive')
                app.mode = 'playerPotionMode'
                return
            #extra energy
            if random.randint(1,4) == 1:
                app.energy += 1
                app.mode = 'playerEnergyBoostMode'
                return
        app.mode = 'opponentDrawCardMode'
            
def opponentDrawCardMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E') 
    drawBoard(app,canvas)
    canvas.create_text(260,200,text = "<------ CLICK DECK TO DRAW OPPONENTS CARD", font = 'Arial 12 bold')
def opponentDrawCardMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if 50 <= app.cx <= 125 and 150 <= app.cy <= 250:
        #app.click.start()
        if len(app.opponentbench) < 5:
            app.opponentbench.append(random.choice(app.opponentpokemonlist))
            app.opponentpokemonlist.remove(app.opponentbench[len(app.opponentbench)-1])
            #MAX HP BOOST POWERUP
            if random.randint(1,7) == 1:
                app.opponentbench[len(app.opponentbench)-1].HP = int((app.opponentbench[len(app.opponentbench)-1].HP)*1.33)
                app.mode = 'opponentHpBoostMode'
                return
            #attackboost
            if random.randint(1,7) == 1:
                for moves in app.opponentbench[len(app.opponentbench)-1].moves:
                    moves.damage = int((moves.damage)*1.33)
                app.mode = 'opponentDamageBoostMode'
                return
            if random.randint(1,6) == 1:
                app.opponentpotions.append('heal')
                app.mode = 'opponentPotionMode'
                return
            if random.randint(1,5) == 1:
                app.opponentpotions.append('hyper potion')
                app.mode = 'opponentPotionMode'
                return
            if random.randint(1,4) == 1:
                app.opponentpotions.append('revive')
                app.mode = 'opponentPotionMode'
                return
        app.mode = 'battleMode'


###############
#selectMode
###############
def selectMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,50,text = 'Which card do you want to place on the battlefield?' , font = 'Arial 24 bold')
    x = 500
    y = 150
    for pokemon in app.pokemondeck:
        canvas.create_rectangle(x-75,y-25,x+75,y+25,width = 3, fill = "light blue")
        canvas.create_text(x,y,text = pokemon.name, font = 'Arial 18 bold', fill = 'dark blue')
        y += 60
def selectMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    #7 if statements for which pokemon I want to choose as my starting one
    if 425 <= app.cx <= 575 and 125 <= app.cy <= 175:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[0])
        app.pokemondeck.pop(0)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 185 <= app.cy <= 235:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[1])
        app.pokemondeck.pop(1)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 245 <= app.cy <= 295:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[2])
        app.pokemondeck.pop(2)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 305 <= app.cy <= 355:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[3])
        app.pokemondeck.pop(3)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 365 <= app.cy <= 415:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[4])
        app.pokemondeck.pop(4)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 425 <= app.cy <= 475:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[5])
        app.pokemondeck.pop(5)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    if 425 <= app.cx <= 575 and 485 <= app.cy <= 535:
        #app.click.start()
        app.battlefield.append(app.pokemondeck[6])
        app.pokemondeck.pop(6)
        for pokemon in app.pokemondeck:
            app.prizecards.append(pokemon)
        app.mode = 'drawCardMode'
    app.opponentbattlefield.append(app.opponentdeck[random.randint(1,6)])
    app.opponentdeck.remove(app.opponentbattlefield[0])
    for pokemon in app.opponentdeck:
        app.opponentprizecards.append(pokemon)
    

#################
#MAIN MODE
#################
def mainMode_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    #import board
    canvas.create_image(320, 293.5, image=ImageTk.PhotoImage(app.playingmat))
    #make my deck
    canvas.create_image(588, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(590, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(592, 388, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(594, 388, image=ImageTk.PhotoImage(app.pokemoncard))

    #make opponent deck
    canvas.create_image(52, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(54, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(56, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    canvas.create_image(58, 199, image=ImageTk.PhotoImage(app.pokemoncard))
    #GUI 
    canvas.create_text(800,380,text = "<------ CLICK DECK TO DRAW YOUR STARTING HAND", font = 'Arial 12 bold') 
def mainMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    #Draws yours and opponents first 7 cards
    if 550 <= app.cx <= 625 and 338 <= app.cy <= 438:
        #app.click.start()
        for r in range(7):
            app.pokemondeck.append(app.mypokemonlist[random.randint(1,len(app.mypokemonlist)-1)])
            app.mypokemonlist.remove(app.pokemondeck[r])
        for r in range(7):
            app.opponentdeck.append(app.opponentpokemonlist[random.randint(1,len(app.opponentpokemonlist)-1)])
            app.opponentpokemonlist.remove(app.opponentdeck[r])
        app.mode = 'selectMode'
#################
# SELECT DIFFICULTY
#################
def selectDifficultyMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,100, text = 'SELECT DIFFICULTY', font = 'Arial 24')
    canvas.create_rectangle(460,180,540,220,width = 3, fill = "green")
    canvas.create_rectangle(460,230,540,270,width = 3, fill = "red")
    canvas.create_text(500,200, text = 'EASY', font = 'Arial 18')
    canvas.create_text(500,250, text = 'HARD', font = 'Arial 18')
    canvas.create_text(500,300, text = 'EASY: Both player and opponent have energy costs, opponent makes random moves, cannot bench pokemon, and can only use powerups, not potions.', font = 'Arial 12 bold')
    canvas.create_text(500,330, text = 'HARD: Opponent has unlimited energy and smartly chooses moves and when to switch a pokemon using an algorithm. Opponent can also use potions.', font = 'Arial 12 bold')
def selectDifficultyMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if 460 <= app.cx <= 540 and 180 <= app.cy <= 220:
        #app.click.start()
        app.difficulty = 'easy'
    if 460 <= app.cx <= 540 and 230 <= app.cy <= 270:
        #app.click.start()
        app.difficulty = 'hard'
    app.mode = 'mainMode'

#################
#login mode
#################
def loginMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_text(500,250, text = 'enter username in terminal', font = 'Arial 24')
def loginMode_keyPressed(app,event):
    if event.key == 'Enter':
        app.mode = 'selectDifficultyMode'
        return
    else:
        app.username += event.key

##################
#leaderboard mode
##################
def leaderboardMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    myData1 = ast.literal_eval(readFile('leaderboard.txt'))
    for key in myData1:
        canvas.create_text(500,293.5,text = f'{key} has the best score of {myData1[key]} turns', font = 'Arial 24 bold')
    canvas.create_text(500,350,text = 'click to go back...', font = 'Arial 12 bold')
def leaderboardMode_mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    app.mode = 'startScreenMode'

#################
#START SCREEN
#################
def startScreenMode_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,1000,587, width = 3, fill = '#F5E97E')
    canvas.create_image(500, 293.5, image=ImageTk.PhotoImage(app.startscreen))
    canvas.create_image(500, 150, image=ImageTk.PhotoImage(app.startscreenlogo))
    canvas.create_image(500, 350, image=ImageTk.PhotoImage(app.startbutton))
    canvas.create_rectangle(420,390,580,430, width = 2, fill = 'light blue')
    canvas.create_text(500, 410, text = 'VIEW BEST SCORE', font = 'Arial 12 bold')
def startScreenMode_mousePressed(app, event):
    app.cx = event.x
    app.cy = event.y
    if 460 <= app.cx <= 540 and 330 <= app.cy <= 370:
        app.mode = 'loginMode'
    if 420 <= app.cx <= 580 and 390 <= app.cy <= 430:
        app.mode = 'leaderboardMode'




##################
#INITIALIZING
##################
#def initiateImages(app):
    #app.battlefieldpokemon = app.loadImage(app.battlefield[0].img)
def appStarted(app):
    readFile('leaderboard.txt')
    #load images syntax taken from cmu 112 website(https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSounds)
    def loadimages(app):
        Charmander.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_9.png')
        Charmander.img = app.scaleImage(Charmander.img, 1/3)
        
        Charmeleon.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_10.png')
        Charmeleon.img = app.scaleImage(Charmeleon.img, 1/3)
        
        Charizard.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/CELC/CELC_EN_4_A.png')
        Charizard.img = app.scaleImage(Charizard.img, 1/3)
        
        Vulpix.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SWSH1/SWSH1_EN_22.png')
        Vulpix.img = app.scaleImage(Vulpix.img, 1/3)

        Ninetales.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY5/XY5_EN_21.png')
        Ninetales.img = app.scaleImage(Ninetales.img, 1/3)

        Growlithe.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_17.png')
        Growlithe.img = app.scaleImage(Growlithe.img, 1/3)

        Arcanine.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY9/XY9_EN_11.png')
        Arcanine.img = app.scaleImage(Arcanine.img, 1/3)

        Magmar.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_20.png')
        Magmar.img = app.scaleImage(Magmar.img, 1/3)

        Ponyta.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_19.png')
        Ponyta.img = app.scaleImage(Ponyta.img, 1/3)

        Rapidash.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY11/XY11_EN_17.png')
        Rapidash.img = app.scaleImage(Rapidash.img, 1/3)

        Bulbasaur.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/BW5/BW5_EN_1.png')
        Bulbasaur.img = app.scaleImage(Bulbasaur.img, 1/3)

        Ivysaur.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM35/SM35_EN_2.png')
        Ivysaur.img = app.scaleImage(Ivysaur.img, 1/3)

        Venusaur.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/CELC/CELC_EN_15_A1.png')
        Venusaur.img = app.scaleImage(Venusaur.img, 1/3)

        Weedle.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_5.png')
        Weedle.img = app.scaleImage(Weedle.img, 1/3)

        Kakuna.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY5/XY5_EN_2.png')
        Kakuna.img = app.scaleImage(Kakuna.img, 1/3)

        Beedrill.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM4/SM4_EN_3.png')
        Beedrill.img = app.scaleImage(Beedrill.img, 1/3)

        Caterpie.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SWSH2/SWSH2_EN_1.png')
        Caterpie.img = app.scaleImage(Caterpie.img, 1/3)

        Metapod.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_4.png')
        Metapod.img = app.scaleImage(Metapod.img, 1/3)

        Butterfree.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM1/SM1_EN_3.png')
        Butterfree.img = app.scaleImage(Butterfree.img, 1/3)

        Tangela.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_8.png')
        Tangela.img = app.scaleImage(Tangela.img, 1/3)

        Squirtle.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM9/SM9_EN_22.png')
        Squirtle.img = app.scaleImage(Squirtle.img, 1/3)

        Wartortle.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/EX14/EX14_EN_43.png')
        Wartortle.img = app.scaleImage(Wartortle.img, 1/3)

        Blastoise.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM9/SM9_EN_25.png')
        Blastoise.img = app.scaleImage(Blastoise.img, 1/3)

        Magikarp.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM115/SM115_EN_15.png')
        Magikarp.img = app.scaleImage(Magikarp.img, 1/3)

        Gyarados.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/HGSS1/HGSS1_EN_4.png')
        Gyarados.img = app.scaleImage(Gyarados.img, 1/3)

        Poliwag.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_23.png')
        Poliwag.img = app.scaleImage(Poliwag.img, 1/3)

        Poliwhirl.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM1/SM1_EN_31.png')
        Poliwhirl.img = app.scaleImage(Poliwhirl.img, 1/3)

        Poliwrath.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_25.png')
        Poliwrath.img = app.scaleImage(Poliwrath.img, 1/3)

        Seel.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_28.png')
        Seel.img = app.scaleImage(Seel.img, 1/3)

        Dewgong.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY10/XY10_EN_16.png')
        Dewgong.img = app.scaleImage(Dewgong.img, 1/3)

        Lapras.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/SM8/SM8_EN_56.png')
        Lapras.img = app.scaleImage(Lapras.img, 1/3)

        Staryu.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY9/XY9_EN_25.png')
        Staryu.img = app.scaleImage(Staryu.img, 1/3)

        Starmie.img = app.loadImage('https://assets.pokemon.com/assets/cms2/img/cards/web/XY12/XY12_EN_31.png')
        Starmie.img = app.scaleImage(Starmie.img, 1/3)
        
    loadimages(app)
    #start screen background
    url = 'https://i.pinimg.com/originals/ab/58/cc/ab58cc75dcb2e42555cf7e614216350a.jpg'
    app.startscreen = app.loadImage(url)
    app.startscreen = app.scaleImage(app.startscreen, 1/1.8)
    url = 'https://cdn.mos.cms.futurecdn.net/nJqzZf3iyhawJfofUMicFV-1200-80.jpg'
    app.startscreenlogo = app.loadImage(url)
    app.startscreenlogo = app.scaleImage(app.startscreenlogo, 1/4)
    #start button
    url = 'https://e7.pngegg.com/pngimages/124/456/png-clipart-button-gamemaker-studio-computer-icons-tk-game-start-button-game-text-thumbnail.png'
    app.startbutton = app.loadImage(url)
    app.startbutton = app.scaleImage(app.startbutton, 1/2)
    #import image
    url = 'https://i.ebayimg.com/images/g/EcIAAOSwmINaz1TG/s-l640.jpg'
    app.playingmat = app.loadImage(url)
    #pokemon card
    url = 'https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pokemon_Trading_Card_Game_cardback.jpg/220px-Pokemon_Trading_Card_Game_cardback.jpg'
    app.pokemoncard = app.loadImage(url)
    app.pokemoncard = app.scaleImage(app.pokemoncard, 1/3)
    #modal app taken from https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSounds
    app.mode = 'startScreenMode'
    #INITIALIZING ALL VARIABLES
    app.battlefield = []
    app.opponentbattlefield = []
    
    app.pokemondeck = []
    app.opponentdeck = []
    
    app.bench = []
    app.opponentbench = []

    app.prizecards = []
    app.opponentprizecards = []
    
    app.opponentpokemons = []
    app.playerpokemons = []

    app.potions = []
    app.opponentpotions = []

    app.opponentattackdamage = 0
    app.playerattackdamage = 0

    app.username = ''

    app.mypokemonlist = ([Charmander,Charmeleon,Charizard,Magikarp,Gyarados,Growlithe,Arcanine,Magmar,Ponyta,Rapidash,Bulbasaur,Ivysaur,Venusaur,Poliwag,Poliwhirl,Poliwrath])

    app.opponentpokemonlist = [Metapod,Butterfree,Tangela,Squirtle,Wartortle,Blastoise,Weedle,Vulpix,Ninetales,Kakuna,Beedrill,Seel,Dewgong,Lapras,Staryu,Starmie,Caterpie]

    app.difficulty = ''

    app.energy = 0
    app.opponentenergy = 0

    #music from https://youtu.be/ufYIjzq_QwA
    pygame.mixer.init()
    app.sound = Sound("pokemonmusic.mp3")
    app.sound.start(loops=-1)

    app.turns = 0


def playPokemon():
    runApp(width=1000, height=587)

playPokemon()



 


