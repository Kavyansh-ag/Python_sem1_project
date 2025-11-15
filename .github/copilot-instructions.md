# AI Coding Instructions for PyProject_Sem1

## Project Overview
This is a Python semester project implementing an **Othello/Reversi board game**. Currently contains a basic `board` class with initial game setup.

## Architecture & Components

### Core Component: `board.py`
- **Class**: `board` - Represents the game board state
- **Grid**: 8x8 array initialized with standard Othello starting position
  - White pieces at (3,3) and (4,4)
  - Black pieces at (3,4) and (4,3)
- **Cell States**: 
  - `'e'` (empty)
  - `'w'` (white)
  - `'b'` (black)

### Current Issues
- `__init__` has syntax error: `[[for _ in range(8)]` should be `[[self.empty for _ in range(8)]`
- Grid initialization hardcoded to 8x8 (size parameter unused)

## Development Patterns

### Code Style
- Class names use lowercase (`board` not `Board`)
- Cell state constants as class attributes
- String-based cell representation (not enums)

### Next Steps (Likely)
When extending this project, expect to implement:
1. Move validation logic (checking valid moves for current player)
2. Board display/rendering methods
3. Game logic for piece flipping
4. Turn management and game state tracking

## Git Workflow
- Repository: `t3ja5-s1ngh/PyProject_Sem1`
- Branch: `main`
- Typical semester project structure (minimal dependencies)

## Debugging Tips
- Game logic will revolve around 8x8 board indexing
- Othello rules: capture opponent pieces by surrounding them
- Test initial board state before implementing move logic
