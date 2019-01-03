Title: Python Arcade Review
Date: 2018-12-16 10:30
Category: Code
Tags: code, python, games
Image: images/python_arcade_review/preview.gif

## TL;DR

- [Arcade](http://arcade.academy) is a wonderfully documented library, that has a very clear idea of it's audience and provides delightful resources to support them.
- Concrete examples help first time readers orientate themselves.
- Using **Arcade** I made a simple 2D game: [Rabbit Herder](https://github.com/ryancollingwood/arcade-rabbit-herder) for fun, and to learn a simple library for drawing primitive shapes - *squares, circles, etc*.
- Describing your data (ie. levels and sprites) as simply as possible makes rapid iteration possible - but only if your data can be represented simply.
- Python has some implications for games development:
    - **Helpful**: Python type system is forgiving and allows you to introduce arbitrary properties without having to specialise entities or introduce additional complexity.
    - **Not Helpful**: The rate of updates demanded by interactive applications would be a challenge in standard Python.

## Why?

![Preview of Rabbit Herder game](images/python_arcade_review/preview.gif)

Sometimes you need a break from giving computers instructions such as: *"display the sum of expenses for the last month"* or *"download a file from this place and put it in this other place"*. In an effort to escape this tedium I figured it would be a refreshing break to give the computer different instructions: *"draw a square and move 5 pixel to the right every 1 second"*.
Additionally learning the in and outs of a Python library for drawing and animating shapes could be helpful for data visualisation purposes in the future.

At first I was tinkering with [PyGame](https://www.pygame.org), which is fully realised framework for developing interactive applications (aka games) in Python. However despite vibrant community and active development, the supporting documentation for **PyGame** was *ehhhhh*. It's functional, you'll find a descriptions of what the various functions do - but not a lot of guidance on how to combine these functions together to make something greater than the sum of the parts.

This is in my opinion the cardinal sin of any documentation, not providing concrete examples of achieving something that is of general interest to the readers of your documentation. Especially when the reader is trying orientate themselves in a new strange land.

I soon discovered [Arcade](http://arcade.academy) and after reading through it's documentation, and more importantly the abundance of simple and to the point examples, I decided to use Arcade for making a simple 2 dimensional game.

## Things that went well

**Drawing Shapes** is super easy with Arcade and given that I am a human of limited graphical skills, being able to programmatically "draw" using squares allowed me to move onto oher things, without agonising over licensing or creating graphical assets.

**Numpy** backed grid for representing the game state, as grids can be expressed as arrays and Numpy does array data structures really efficiently compared to using `list` or some other python standard collection. There are some tradeoffs:
- Your grid will have to be a fixed size, however given that devices have a fixed amount RAM (although no where near the challenge of the 640k barrier), learning to be succient in your world building or developing a way to swap in and out segments of the game is unavoidable. So a fixed size representation of the game world isn't a constraint that using Numpy introduced.
- Initially wrapping your head around the way you'll be accessing your data in a multi-dimensional numpy grid can be cumbersome to start with. Given my grid design was `height * width * layers` determining if there is a wall at a given row and column takes a moment to get right.

**Weak Typing**, I was able to specialise my data structures where it made sense and NOT specialise where I felt it was a little too narrow. For example when I wanted to keep track of which carrots had been placed by the player (and thus shouldn't be picked up by the player again), I was able to assign a `player_placed` attribute on carrots, which did not modify the definition of all other entities (carrots, rabbit, player, wall).
or game development in strongly typed languages what I've observed is either a new class is created to deal with the specialisation or to use an [entity component system](https://en.wikipedia.org/wiki/Entity%E2%80%93component%E2%80%93system). ECS do have other advantages, particularly for concurrent evaluation of entity state and is still a worthwhile pattern in weakly typed environments.

## Things that didn't go well

**Collision detection**, I implemented my own rather than using the provided collision detection as I wanted to keep a loose coupling from my game code and Arcade. I could have still achieved this loose possibly through an event based design, raising an event when a moveable entity attempts moves to a grid position and then allowing Arcade collision detection to step and in and raise further events if required.

## Things I have mixed feelings about

**Loose Coupling** - I managed to keep my game logic implementation completely separate from Arcade as was I wasn't enitrely sure Arcade was going to do what I needed it do. I was fairly (90%) confident given the great documentation and examples available on the project's Web site. However as they say, the proof is in the pudding. Thus the code was structured in a way that if I needed to switch to some other framework (or if I was really feeling like a challenge going full DIY) I wouldn't have to unpick the Arcade specific code from my own.
Like all decisions there was a tradeoff, as I had to write some code to translate between my generic values and Arcade's specific values for fundamental concepts such as colours and keyboard keys.

**Arcade does horizontal placement from the bottom up**. If you've done software development around the 2 dimensional placement of things on screen (i.e. web-design, graphic editing, other game frameworks), you've probably worked with pixel co-ordinates `(0,0)` being the top-left position on your screen. Not the case in Arcade, pixel position `(0,0)` is the bottom-left position on your screen. Having read into the motivations of the Arcade project as an educational tool bottom-left is better aligned with the way co-ordinate systems are taught in schools. It wasn't impossible to get around, but still an annoyance.


## Take-Aways

Frameworks are always a trade-off, are you willing to accept the choices made for you by the framework for benefit of being able to outsource your responsibility. The trade-offs you'll have to make to use Arcade are sensible, and the benefits you receive in exchange are worth it.

If you're looking for a fun project, or a new python library for interactive applications (aka games), I recommend you give it a try.