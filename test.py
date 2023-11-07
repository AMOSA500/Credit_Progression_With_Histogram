from graphics import *

# Create a window
win = GraphWin("Histogram", 400, 400)
win.setCoords(0, 0, 400, 400)
win.setBackground("white")

# Data for the histogram
data = [10, 20, 15, 30, 25]

# Bar width and spacing
bar_width = 30
bar_spacing = 10  # Adjust this value to control the space between bars

x = bar_spacing  # Start with initial spacing

for value in data:
    # Create a bar using the specified width and spacing
    bar = Rectangle(Point(x, 0), Point(x + bar_width, value))
    bar.setFill("blue")
    bar.draw(win)

    # Add labels at the bottom of each bar
    label = Text(Point(x + bar_width / 2, -10), "Label")
    label.setSize(8)
    label.draw(win)

    # Add top text above each bar
    top_text = Text(Point(x + bar_width / 2, value + 5), str(value))
    top_text.setSize(10)
    top_text.draw(win)

    # Add bottom text below each bar
    bottom_text = Text(Point(x + bar_width / 2, -20), "Bottom Text")
    bottom_text.setSize(8)
    bottom_text.draw(win)

    # Update the x position for the next bar
    x += bar_width + bar_spacing

win.getMouse()
win.close()
