# CrowdControlInMarvelRivals

Have you ever wondered how much crowd control (CC) is in Marvel Rivals? Being a tank player, I definitely have... way too frequently. I have sunk too much time and money on this game for tenacity to not proc. 

This project analyzes crowd control abilities across Marvel Rivals' hero roster to quantify just how much CC tanks (and everyone else ig) have to deal with.

## Overview

I went through every character and tested their abilities on another character / bot in the firing range to see if they have any Crowd Control effects. The data was recorded and stored the the MRCC excel sheet. 

## Motivation

Unfortunately with the addition of every new character every half-season, NetEase loves giving them some sort of crowd control for some reason. Thus, the game will at some point be overwhelming with random CC and moving your left stick or pressing WASD will not determine how much distance you can cover. Tenacity also never procs for some reason on tanks, even though they get CC dumped half the time. Frankly, I started this project to justify my anguish of playing tank lol. Here is [Exhibit A](https://www.youtube.com/watch?v=G1_xhNsUyfM). Keep in mind that this was pre-tenacity update.

## Data

- **Source**: Primarily in-game Testing (For some reason, NetEase forgets to indicate that some abilities have CC in the character ability menu) 
- **Scope**: For the sake of this project, CC is defined as any effect that hinders an opposing player to moving freely. Examples of this are grounded, slowed, stunned, etc.
- **Format**: Raw data is stored in a Microsoft Excel sheet, going from passive to ultimate. 

## Methodology

There are a lot of CC "types" in Marvel Rivals and it would be very time-consuming to list EVERY SINGLE ONE, so I just made categories to classify the effect it had on the player. This is listed on the txt file but this is how I personally defined them...

* Launched: Describes when an opposing player is vertically displaced
* Pushed: Describes when an opposing player is horizontally displaced away from acting player
* Cutscene:	Describes when an opposing player is displaced whilst losing full control
* Stunned: Describes when an opposing player cannot move, but retains the same position prior to action 
* Slowed:	Describes when an opposing player is capable of movement, but at a slower pace than normal
* Grounded:	Describes when an opposing player strictly cannot use movement abilities
* Pulled:	Describes when an opposing player is displaced towards the acting player
* Stuck: Describes when an opposing player cannot move, but can still interact with the acting player
* Exile: (Hulk) Describes when an opposing character is effectively removed from the game until hulk interacts with exiled opponent or until time runs out on exile

Something to note here is that even though exile could technically fall under "cutscene," I made it its own category because exile temporarily removes the interaction of the affected player from both non-Hulk players AND objective. 

## Results

With 53 total characters (14 vanguards, 26 duelists, 12 strategists, and DP) with the release of The Hood, there is a lot to learn about the CC condition in Marvel Rivals.

### Character Count by Role

| Role | Value |
|---|---|
| All Three | 1 |
| Duelist | 26 |
| Strategist | 12 |
| Vanguard | 14 |

### Mean CC Abilities by Role

| Role | Value |
|---|---|
| All Three | 0.000000 |
| Duelist | 1.384615 |
| Strategist | 1.250000 |
| Vanguard | 2.428571 |

### Standard Deviation of CC Abilities by Role

| Role | Value |
|---|---|
| All Three | NaN |
| Duelist | 1.061204 |
| Strategist | 1.544786 |
| Vanguard | 1.222500 |

### Highest CC Count from a Single Character by Role

| Role | Value |
|---|---|
| All Three | 0 |
| Duelist | 3 |
| Strategist | 5 |
| Vanguard | 4 |

### Biggest Culprits by Role

| Role | Value |
|---|---|
| All Three | Deadpool |
| Duelist | Elsa Bloodstone, Mister Fantastic, Spider-Man, Winter Soldier |
| Strategist | Invisible Woman |
| Vanguard | Bruce Banner, Rogue |

### Overall Top CC Character

| Character | Number of CC Abilties |
|---|---|
| Invisible Woman | 5 |

### CC Effect Frequency

| Role | Value |
|---|---|
| Slowed | 22 |
| Pushed | 21 |
| Cutscene | 17 |
| Launched | 16 |
| Stunned | 10 |
| Stuck | 10 |
| Pulled | 8 |
| Grounded | 5 |
| Exile | 1 |

**Total CC Abilities in Game:** 85

## Tech Stack

- Language(s) used: Python
- Libraries: Pandas

## How to Run

1. **Clone the repo**
```bash
   git clone https://github.com/MostafaSSh/CrowdControlInMarvelRivals.git
   cd CrowdControlInMarvelRivals
```

2. **Install dependencies**
```bash
   pip install pandas openpyxl
```

3. **Run the script**
```bash
   python MRCC.py
```

   This reads from `MRCC.xlsx` and generates `MRCC_Updated.xlsx` with the processed crowd control data.

4. **Data reference**

   See `CC Definitions.txt` or the Methodologies section above for how crowd control types are categorized in this analysis.
   
## Future Work

With the statistics (mostly) complete, I will write a report to discuss my findings.

## Author

Mostafa Shalan — [LinkedIn](https://linkedin.com/in/mostafa-s-shalan) · [Portfolio](https://github.com/MostafaSSh)
