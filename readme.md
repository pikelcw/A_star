# A* Path Finding
This program use A* algorithm to find a path between starting point and end point. Have an option to keep the path as faraway from wall as possible.

## Getting Started
### Prerequisites
This project needs numpy and matplotlib.

### Creating your own maze
You can add your own map, in csv format, to *data* folder.
- 1 for wall
- 0 for walkable space
- 2 for start point
- 3 for end point.

### Solve the maze
You can choose to keep the path away from wall by adding `--keepDistance` or `-kd` flag. 

The `--verbose` or `-v` flag can animate the solving process in realtime.
```
python3 A_star.py --keepDistance --verbose mapName.csv
```

