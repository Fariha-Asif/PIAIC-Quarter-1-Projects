import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40


def on_hover(event):
    """Temporarily change the color of the rectangle to white on hover."""
    widget = event.widget
    item = widget.find_withtag("current")  # Get the item under the cursor
    if item:  # Check if there is a valid item
        current_color = widget.itemcget(item, "fill")
        if current_color != "white":  # Only change color if it's not already white
            widget.itemconfig(item, fill="lightgray")


def on_leave(event):
    """Reset the color of the rectangle when the mouse leaves, unless it was clicked."""
    widget = event.widget
    item = widget.find_withtag("current")  # Get the item under the cursor
    if item:  # Check if there is a valid item
        current_color = widget.itemcget(item, "fill")
        if current_color == "lightgray":  # Reset to blue only if it wasn't clicked
            widget.itemconfig(item, fill="blue")


def on_click(event):
    """Permanently change the color of the rectangle to white on click."""
    widget = event.widget
    item = widget.find_withtag("current")  # Get the item under the cursor
    if item:  # Check if there is a valid item
        widget.itemconfig(item, fill="white")  # Permanently set to white


def main():
    root = tk.Tk()
    root.title("Interactive Grid with Hover and Click Effects")
    
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack()
    
    # Create grid of rectangles
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", tags="rect")
    
    # Bind hover events
    canvas.tag_bind("rect", "<Enter>", on_hover)  # Trigger when the mouse enters a rectangle
    canvas.tag_bind("rect", "<Leave>", on_leave)  # Trigger when the mouse leaves a rectangle
    
    # Bind click event
    canvas.tag_bind("rect", "<Button-1>", on_click)  # Trigger when a rectangle is clicked
    
    root.mainloop()


if __name__ == '__main__':
    main()
