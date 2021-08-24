# Search Algorithms

## Overview

In this project, we want to solve a card game with three search algorithms.  
We want to sort cards by their number, but we must also put cards with same color in one column.
In input we get an initial form of cards that we must change this form and reach our target form.  

> Our target form is **not unique**

> Input system is **same** for all alghorithms

## Sample

For input form, in first line we provide three numbers:   
**Columns count, colors count, max number**  
After that for each columns, we must put cards.  
For a single card we using this format: **number + color character**  
And also for empty column we using **#** character.  

Here we can see some sample of input and corresponding outputs.  

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
