# Constraints Based Ranking

## TL-DR:
**Why**:
constraints based reasoning, imperitive coding, parsing text into instructions for a computer, and how I put it together in an interactive application you could use for prioritising.

## Background

Prioritisation (ranking) is something I have to deal with daily. The magnitude and complexity of it varies, and most times it's usually something I can resolve with some index cards and a sharpie pen.

However, as the number of things to choose between increases and certainty decreases, even getting an approximate course of action can be difficult.

For example given the following conditions
- **Drink tea** not first
- **Boil water in the kettle** not last
- **Boil water in the kettle** before **Pour boiled water into cup**
- **Get a cup from the cupboard** before **Pour boiled water into cup**
- **Put tea bag into cup** after **Get a cup from the cupboard**
- **Put tea bag into cup** before **Drink tea**
- **Pour boiled water into cup** before **Drink tea**

You could spend some figuring this out and come up with some thing like this:
![The ways to make a cup of tea - no milk for me!]({static}/images/constrains_based_ranking/tea_graphviz.png)

Thankfully we have computers for whom recalling large lists of things is a trivial matter.

## Constraints Based Problem Solving

To solve a problem like this, I turned to using the `python-constraints` package, and based my To see the documentation for this class, refer to: [Python Constraints Problem API](http://labix.org/doc/constraint/public/constraint.Problem-class.html)

For a an overview how to install and use this package have a look at this post from [stackabuse.com].(https://stackabuse.com/constraint-programming-with-python-constraint/)

The idea is that we have a **Problem** which consists of **Variables** (which are numeric) and **Constraints**. In solving the Problem, we will be given the permutations of the Variables that satisfy the Constraints.
Given we have a collection of things (steps for making tea) and I'm want to know potential order of operations (so assigning a number to each step) - this paradigm works for the simple tea scenario.

So with this in mind I created a RankProblem class that inherits from the Problem class which to solve the above tea steps looks like:

```python
def solve_tea():
    ranking_problem = RankingProblem()

    ranking_problem.set_items([
        "Boil water in the kettle",
        "Pour boiled water into cup",
        "Get a cup from the cupboard",
        "Put tea bag into cup",
        "Drink tea",
    ])

    ranking_problem.not_first("Drink tea").\
        not_last("Boil water in the kettle").\
        is_before("Boil water in the kettle", "Pour boiled water into cup").\
        is_before("Get a cup from the cupboard", "Pour boiled water into cup").\
        is_after("Put tea bag into cup", "Get a cup from the cupboard").\
        is_before("Put tea bag into cup", "Drink tea").\
        is_before("Pour boiled water into cup", "Drink tea")

    solutions = ranking_problem.solve()
    print(solutions)
```

Which looks something like:
```python
(
  [
    "Boil_water_in_the_kettle",
    "Get_a_cup_from_the_cupboard",
    "Pour_boiled_water_into_cup",
    "Put_tea_bag_into_cup",
    "Drink_tea"
  ],
  [
    "Boil_water_in_the_kettle",
    "Get_a_cup_from_the_cupboard",
    "Put_tea_bag_into_cup",
    "Pour_boiled_water_into_cup",
    "Drink_tea"
  ],
  [
    "Get_a_cup_from_the_cupboard",
    "Boil_water_in_the_kettle",
    "Pour_boiled_water_into_cup",
    "Put_tea_bag_into_cup",
    "Drink_tea"
  ],
  [
    "Get_a_cup_from_the_cupboard",
    "Boil_water_in_the_kettle",
    "Put_tea_bag_into_cup",
    "Pour_boiled_water_into_cup",
    "Drink_tea"
  ],
  [
    "Get_a_cup_from_the_cupboard",
    "Put_tea_bag_into_cup",
    "Boil_water_in_the_kettle",
    "Pour_boiled_water_into_cup",
    "Drink_tea"
  ]
)
```

The challenge is solved both through a imperative and declarative means.

The class `RankingProblem` is the imperative interface, as defined in 'solver/ranking_problem.py'

This class is descendant of the `Problem` from the `python-constraints` package. To see the documentation for this class, refer to: [Python Constraints Problem API](http://labix.org/doc/constraint/public/constraint.Problem-class.html)

## Declarative Problem Solving

Declarative solving is achieved using the PLY (Python Lex-Yacc) module. To see a detailed overview of the module and it's usage: [PLY Overview](https://www.dabeaz.com/ply/ply.html#ply_nn2).

