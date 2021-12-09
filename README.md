# Projeckt_Map

## About ##
Create your own custom terrain map in 2D 

## Setup ##
If you want to build up a virtual environment, [go here](https://virtualenv.pypa.io/en/latest/installation.html#via-pip). Alternatively, you may utilize my built-in environment by unzipping the **env** folder.

- Create your working environment and virtualenv:
```
$ virtualenv environment
```
- activating virtualenv:
```    
$ source environment/bin/activate
$ cd src
```
- installing requirements:
```    
$ pip install -r requirements.txt
```
- Run gui:
```    
$ python gui.py
```

## How it works ##

**Seed** :
- Establishes the random number generator's initial state. You may alter it to generate a different random pattern in your image.

**Color Range** :
- The Color Range picks a specific color or range of colors within an existing selection or a full picture.

**Scale** :
- The number that specifies how far away the noisemap should be viewed.

**Lacunarity** :
- The amount of information added or subtracted at each octave is determined by this number (adjusts frequency).

**Persistence** :
- The number indicating how much each octave contributes to the overall structure (adjusts amplitude).

**Octaves** :
- The amount of detail levels you desire in your noise.

**Threshold** :
- It restricts the threshold per color, similar to a sea level.
