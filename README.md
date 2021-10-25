[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

# Search Algorithms

## Overview

In this project, we want to solve a card game with three search algorithms.  
In this card game, we have to sort our cards by their number in descending order, and we must also assure that all cards in one row are of the same color. In our input we get an initial configuration of cards, in which we must change this form to reach our desired target form.

> We can only remove cards from the bottom of each row and add it to the bottom of another row. No other moves are allowed.

> Our target form is **not unique**

> Input system is **same** for all alghorithms

## Sample

For input form, in first line we receive three numbers:   
**Rows count**, **colors count**, and **max number** of cards in each row.  
After this line, we receive the current configuration of cards, line by line. (each line corresponding to one row.)   
For every single card, we use the following format: **number + color character**. (e.g, 3r indicates a card which has number 3 and is red.)  
If we have any empty rows left, they will be shown with **#** characters.  

Here we can see some samples of input and their corresponding output.  

### Input
```
4 2 3
3r 1r 2r
3b 1b 2b
#
#
```

### Output
```
Target is :
-------------------
3r 1r
3b 1b
2r
2b
-------------------
Target depth is 2
Move from 1th row to 3th row
Move from 2th row to 4th row
Explored nodes are 19
Created nodes are 24
```

### Input
```
4 2 5
5g 4g 3g 2r 1g
5r 4r 3r 2g 1r
#
#
```

### Output
```
Target is :
-------------------
5g 4g 3g 2g
5r 4r 3r
1g
2r 1r
-------------------
Target depth is 4
Move from 1th row to 3th row
Move from 1th row to 4th row
Move from 2th row to 4th row
Move from 2th row to 1th row
Explored nodes are 60
Created nodes are 132
```
[forks-shield]: https://img.shields.io/github/forks/KoroshRH/SearchAlgorithms.svg?style=for-the-badge
[forks-url]: https://github.com/KoroshRH/SearchAlgorithms/network/members
[stars-shield]: https://img.shields.io/github/stars/KoroshRH/SearchAlgorithms.svg?style=for-the-badge
[stars-url]: https://github.com/KoroshRH/SearchAlgorithms/stargazers
[issues-shield]: https://img.shields.io/github/issues/KoroshRH/SearchAlgorithms.svg?style=for-the-badge
[issues-url]: https://github.com/KoroshRH/SearchAlgorithms/issues
[license-shield]: https://img.shields.io/github/license/KoroshRH/SearchAlgorithms.svg?style=for-the-badge
[license-url]: https://github.com/KoroshRH/SearchAlgorithms/blob/master/LICENSE
