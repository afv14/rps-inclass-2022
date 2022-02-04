# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

## Setup

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```

## Usage

Run the rock paper scissors game:

```sh
python game.py
```

Included in this rock paper scissors game is the option for a user to pass an enviromental variable through the command line terminal. A player is free to set their username as demonstrated below:

```sh
USERNAME="Dolly Parton" python game.py
```

## Testing

Run tests:

```sh
pytest
```



