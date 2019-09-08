# Constraints Based Ranking

## TL-DR:
**Why**:
constraints based reasoning, imperitive coding, parsing text into instructions for a computer, and how I put it together in an interactive application you could use for prioritising.

## Background

Prioritisation (ranking) is something I have to deal with daily. The magnitude and complexity of it varies, and most times it's usually something I can resolve with some index cards and a sharpie pen.

However, as the number of things to choose between increases and certainty decreases, even getting an approximate course of action can be difficult.

For example given the following conditions
- **Drink tea** cannot be first
- **Boil water in the kettle** cannot be last
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

We could solve this problem through explicitly telling the computer through a code interface, such as:

The challenge is solved both through a imperative and declarative means.

The class `RankingProblem` is the imperative interface, as defined in 'solver/ranking_problem.py'

This class is descendant of the `Problem` from the `python-constraints` package. To see the documentation for this class, refer to: [Python Constraints Problem API](http://labix.org/doc/constraint/public/constraint.Problem-class.html)

## Declarative Problem Solving

Declarative solving is achieved using the PLY (Python Lex-Yacc) module. To see a detailed overview of the module and it's usage: [PLY Overview](https://www.dabeaz.com/ply/ply.html#ply_nn2).

