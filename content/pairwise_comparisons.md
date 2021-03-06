title: Choices Don't Have to be Hard
date: 2019-02-21 20:53
category: Requirements
tags: requirements, analysis
cover_image: images/pairwise_comparisons/which_floof.gif
description: Breaking your choices down to series of pairwise comparisons can facilitate making value based decisions.

## TL;DR
- Value based decisions, being decisions that cannot be reduced to numerical expression can be difficult.
- Decomposing the properties or options of the decision into pairs allows us to score our decisions.
- I'll demonstrate how to do this, both in process and with a simple code example. 

Sometimes choices are easy. Cheese burger or double cheese burger? Easy, how hungry are you? 

As the number of differences between our options increase the more complex the decision becomes. If the number of choices increases from two, well it starts to get out of hand.
Finally if this wasn’t enough when the choices are qualitative (how do I *feel* about it) than quantitative, how do you even establish a basis of comparison? 
For example, how could you go about choosing a type of pet?
![Cats or Dogs? Why can't we all get along.]({static}/images/pairwise_comparisons/which_floof.gif)

## Value Based Decisions

As Ruth Chang states in a TED talk: 
> *“We unwittingly assume that values like justice, beauty, kindness, are akin to scientific quantities, like length, mass and weight... As post-Enlightenment creatures, we tend to assume that scientific thinking holds the key to everything of importance in our world, but the world of value is different from the world of science. The stuff of the one world can be quantified by real numbers. The stuff of the other world can’t.”*

[!embed](http://www.youtube.com/watch?v=8GQZuzIdeQQ)

Not to be contrary to Ruth's ideas (it's a really good talk you should watch it) we can apply some “scientific” thinking to facilitate value based decision making.

## Framework For Value Based Decisions

The [Analytical Hierarchy Process](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) is a framework for making complex decisions. At the heart of the framework is the notion of 
pairwise comparisons.
By evaluating all possible pair combinations for the criteria and/or options under consideration we are able to score of our preferences. Thus we’ll be better positioned to make a decision.

So let’s demonstrate this technique in choosing a pet. 

Write out each option on an index card, laying them out horizontally.
![Laying out our options on index cards]({static}/images/pairwise_comparisons/pairwise_01.png)


Write the leftmost option and the option right of it on a new index card.
![Writing our first pair of options]({static}/images/pairwise_comparisons/pairwise_02.png)


Then write the leftmost option and the option that second over right of it.
![Writing our second pair of options]({static}/images/pairwise_comparisons/pairwise_03.png)


Then move once right from the left most option and repeat. It might be easier to illustrate with an animation:
![Repeating the process]({static}/images/pairwise_comparisons/pairwise_combinations_construction.gif)


Then pick up all the index cards you’ve written a pair of options on and shuffle them (perhaps let someone else shuffle them). Then pick an index card and circle the option you prefer. 

The key here is *preferences*, you may pick up a card where you don’t care for either option, but it’s not about picking the best option overall. It’s about about picking the option you preferred from the two presented. **Similarly resist the urge to pick both**. If you’re really struggling to only pick one, then perhaps you need to detail the criteria you’re considering a look to using the full Analytical Hierarchy Process.

Once you’ve chosen your preferred option for every pair tally up the the number of times you’ve chosen each option. Viola! You now have some numbers to aid your decision making.

I’ve included a toy implementation of a pairwise comparison process in Python below:

![Demo of pairwise comparison application]({static}/images/pairwise_comparisons/pairwise_toy_demo.gif)

```python  
import numpy as np
import pandas as pd
from random import shuffle, seed

from itertools import combinations_with_replacement

print("Enter the options as a comma separated string - e.g. dog, cat, pony")
entered_options = input()
if not entered_options:
    entered_options = "Option 1, Option 2, Option 3, Option 4"

options = [x.strip() for x in entered_options.split(",")]

# let's shuffle the options to keep things interesting
shuffle(options)

# the for loop above as a list comprehension using 'combinations_with_replacement'
pairwise_combinations = [x for x in list(combinations_with_replacement(options, 2)) if x[0] != x[1]]

# To save our scores let's construct an empty dataframe

def get_blank_scores(options):
    return pd.DataFrame(
        np.zeros((len(options), len(options))),
        columns = options,
        index = options
    )

# again to keep things interesting let's shuffle the order of the pairwise comparisons.

shuffle(pairwise_combinations)

# Now for each pair we ask which option is preferred.

df = get_blank_scores(options)

for pair in pairwise_combinations:

    lhs = pair[0]
    rhs = pair[1]

    print(f"(a) {lhs} or (b) {rhs}?")
    result = input(">")
    
    # where we choose the lhs over the rhs
    # +1 to it's own row/column
    # whereas if we choose rhs over lhs
    # +1 to it's row but the rhs column
    if result == "a":
        df.loc[lhs, lhs] += 1
    elif result == "b":
        df.loc[lhs, rhs] += 1

print("")
print("=======================")
print("Scores")
print(df)
print("")

# lets summarise and get the highest scoring option(s)
results = df.sum()
max_score = results.max()
best_options = results[results == max_score]

# display a message about the scoring results
if len(best_options) == 0:
    outcome = "No best option after comparing all pairwise combinations"
elif len(best_options) == len(options):
    if max_score > 0:
        outcome = "All options were rated equally, consider some other criteria to evaluate the options by."
    else:
        outcome = "It seems like you didn't vote for any options"
elif len(best_options) > 1:
    outcome = "We have a tie!"
else:
    outcome = "We have a winner!"

print("=======================")
print(outcome)
print("")
for x in dict(best_options):
    print(x, "with", best_options[x], "votes")
```    

Go forth! Divide and conquer!