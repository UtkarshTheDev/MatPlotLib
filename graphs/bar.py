import matplotlib.pyplot as plt
from data.dataframe.data import df

plt.xlabel("Name")
plt.ylabel("ODI")
plt.title("ODI vs Test")

# Bar Graph

## Plotting ODI
# plt.bar(df.Name, df.ODI, color="red", label="ODI")

## Plotting Test
# plt.bar(df.Name, df.Test, color="blue", label="Test")

## Setting Bar Width
# plt.bar(df.Name, df.ODI, color="red", label="ODI", width=0.4)

## Setting Position
# plt.bar(df.Name, df.ODI, color="red", label="ODI", position=0.0)

## Plotting Both
# Get the number of players and create positions for each player
num_players = len(df.Name)  # Total number of players
player_positions = range(num_players)  # Creates positions 0, 1, 2, ...

# Set bar width and calculate offsets
bar_width = 0.4
# Calculate the positions for the ODI bars and the Test bars
# Start with the player positions (0, 1, 2, ...)
# Shift the ODI bars to the left by half of the bar width
# Shift the Test bars to the right by half of the bar width

# This is done by creating a new list of positions for the ODI bars
# This list is created by subtracting half of the bar width from each player position
# The negative sign ensures that the bars shift to the left
odi_positions = [pos - bar_width/2 for pos in player_positions]  # ODI bars shift left

# This is done by creating a new list of positions for the Test bars
# This list is created by adding half of the bar width to each player position
# The positive sign ensures that the bars shift to the right
test_positions = [pos + bar_width/2 for pos in player_positions]  # Test bars shift right

# The resulting lists will have the positions for the ODI bars and the Test bars
# The number of elements in these lists will be the same as the number of players

# Plot ODI bars (red)
plt.bar(odi_positions, df.ODI, width=bar_width, color="red", label="ODI")

# Plot Test bars (blue) - positioned next to ODI bars
plt.bar(test_positions, df.Test, width=bar_width, color="blue", label="Test")

# Set x-axis tick marks at player positions with player names
plt.xticks(player_positions, df.Name)


# Legend
plt.legend(loc="upper right")

plt.show()
