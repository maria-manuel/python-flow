# REMEMBER: Only do one challenge at a time! Save and test after every one.


print('Challenge 1 -------------')
# Challenge 1:
# When programming the first thing you should always do is add a "print" to
# your code. Why? Because it helps catch many mistakes. If you can get it to
# "print" to the terminal, you know you are running the file correctly, and
# that it's "picking up" on the changes you made.

# To help get into that habit, your first challenge is to write Python code to
# print 'Welcome to week 3!', save, and run it.

print('Welcome to week3!')



print('Challenge 2 -------------')
# Challenge 2:
# Create 4 variables:
# "home_team" - the name of your favorite NBA team (or a different sport)
# "rival_team" - the name of a team you dislike
# "home_score" - how many points you want your team to score
# "rival_score" - how many points your opponent scores

home_team = '49ers'
rival_team = 'Cowboys'
home_score = '10'
rival_score = '2'





print('Challenge 3 -------------')
# Challenge 3:
# Uh oh, buggy code! One at a time, uncomment the following lines of code. Each
# one has a single typo or mistake. Fix the mistakes to get it running.
#printer("The most anticipated game today: ", home_team, "vs", rival_team)
#print(home_team, "won against", Rival_Team)
#print(home_team, "managed to score" home_score "points")
# print "The pathetic", rival_team, "only scored", rival_score, "points"

print("The most anticipated game today: ", home_team, "vs", rival_team)
print(home_team, "won against", rival_team)
print(home_team, "managed to score", home_score, "points")
print ("The pathetic", rival_team, "only scored", rival_score, "points")


print('Challenge 4 -------------')
# Challenge 4:
# Using string concatenation operator ("+", or any equivalent method), rewrite
# the print statements to write code that will combine the story as above, and
# instead of outputting it directly to the screen, put it in a variable called
# "story".

# Then, save it to a file called "sports_story.txt"

# Hint: integer and string types cannot be concatenated together without
# converting the integer first into a string. Instead of just home_score, write
# str(home_score) for the string version.

## Notes: () for python keep in view w/i screen; \n for new line

story = (
    "The most anticipated game today: " + home_team + " vs " + rival_team + "\n" +
    home_team + " won against " + rival_team + "\n" +
    home_team + " managed to score " + str(home_score) + " points.\n" +
    "The pathetic " + rival_team + " only scored " + str(rival_score) + " points\n"
)
open('sports_story.txt', 'w+').write(story)




# Advanced Bonus Challenge:
# Time to get practice combining HTML and Python.
# 1. Read in the sports_story.txt
# 2. Transform it so that every line is a paragraph
# 3. Write it to sports_story.html
# 4. Look up how to cause that file to open up in your browser using Python



