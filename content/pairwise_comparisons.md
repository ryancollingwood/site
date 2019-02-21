title: Choices don't have to hard
date: 2019-02-21 20:53
category: Requirements
tags: requirements, analysis
cover_image: images/pairwise_comparisons/which_floof.gif
description: Breaking your choices down to series of pairwise comparisons can facilitate making value based decisions. 

Sometimes choices are easy. Cheese burger or double cheese burger? Easy, how hungry are you? 

As the number of differences between our options increase the more complex the decision becomes. If the number of choices increases from two, well it starts to get out of hand.
Finally if this wasn’t enough when the choices are qualitative (how do I *feel* about it) than quantitative, how do you even establish a basis of comparison? 

As Ruth Chang states in a TED talk: 
> “We unwittingly assume that values like justice, beauty, kindness, are akin to scientific quantities, like length, mass and weight... As post-Enlightenment creatures, we tend to assume that scientific thinking holds the key to everything of importance in our world, but the world of value is different from the world of science. The stuff of the one world can be quantified by real numbers. The stuff of the other world can’t.”

https://youtu.be/8GQZuzIdeQQ

It is possible to use “scientific” thinking to facilitate value based decision making.
The [Analytical Hierarchy Process](https://en.wikipedia.org/wiki/Analytic_hierarchy_process) is a framework for making complex decisions. At the heart of the framework is the notion of 
pairwise comparisons.
By evaluating all possible pair combinations for the criteria and/or options under consideration we are able to score of our preferences. Thus we’ll be better positioned to make a decision.

So let’s demonstrate this technique in choosing a new type of pet. 

Write out each option on an index card, laying them out horizontally.
![Laying out our options on index cards]({static}/images/pairwise_comparisons/pairwise_01.png)


Write the leftmost option and the option right of it on a new index card.
![Writing our first pair of options]({static}/images/pairwise_comparisons/pairwise_02.png)


Then write the leftmost option and the option that second over right of it.
![Writing our second pair of options]({static}/images/pairwise_comparisons/pairwise_03.png)


Repeat. It might be easier to illustrate with an animation:
![Repeating the process]({static}/images/pairwise_comparisons/pairwise_combinations_construction.gif)


Then pick up all the index cards you’ve written a pair of options on and shuffle them (perhaps let someone else shuffle them). Then pick an index card and circle the option you prefer. 

The key here is preferences, you may pick up a card where you don’t care for either option, but it’s not about picking the best option overall. It’s about about picking the option you preferred from the two presented. Similarly resist the urge to pick both. If you’re really struggling to only pick one, then perhaps you need to detail the criteria you’re considering a look to using the full Analytical Hierarchy Process.

Once you’ve chosen your preferred option for every pair tally up the the number of times you’ve chosen each option. Viola! You now have some numbers to aid your decision making.

I’ve included a toy implementation of a pairwise comparison process in Python below:


Divide and conquer!
