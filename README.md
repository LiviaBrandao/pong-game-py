# pong-game-py
Pong Game developed using Python, embbeded systems class 2020.
https://github.com/LiviaBrandao/pong-game-py/blob/master/assets/kitty.gif
https://github.com/LiviaBrandao/LiviaBrandao/blob/master/assets/kitty.gif

## Running the Project
Besides having Python installed, you need to execute the following command

``` python 
pip install pygame
```

This will install the pygame library.

## The game must look like this
![Screenshot](https://github.com/LiviaBrandao/pong-game-py/blob/master/assets/gameScreenshot.png)

## More about the logic behind

``` python

ballCollision {
  - Check if the ball is hitting one of the walls
    - If it hit the left wall, reflect to the right
    - If it hit the right wall, reflect to the left
    - If it hit the bottom wall, reflect upwards
    - If it hit the top wall, reflect downwards

  - Check if the ball is hitting one of the paddles
    - If the ball is on the right (r1)
      - If it hit the top of the paddle, reflect downwards to the left
      - If it hit the bottom of the paddle, reflect upwards to the left
    - If the ball is on the left (r2)
      - If it hit the top of the paddle, reflect downwards to the right
      - If it hit the bottom of the paddle, reflect upwards to the right
}

paddleCollision (ballPosition x and ballPosition y) {
  - If it hit on top
  - If it hit on the bottom
}

```
