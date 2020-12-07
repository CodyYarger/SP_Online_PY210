# 12/04/2020
# Dev: Cody Yarger
# lesson02: Grid Printer Function

# This script includes a print_grid function that prints a grid to the screen.
# The function takes two arguments row_col and cell_size. row_col indicate the number of rows and
# columns and cell_size indicates the cell size.

def grid_printer(row_col, cell_size):
    """ This function prints a grid to the screeen and takes number of rows and
     columns and cell size arguments (row_col), (cell_size)"""

    # print +- row border pattern for given cell size and number of rows and columns
    for i in range(row_col):
        print(row_col*("+" + "-"*cell_size) + "+")

        # print | column borders for given cell size and number of rows and columns
        for i in range(cell_size):
            print(row_col*("|" + " "*cell_size) + "|")

    # print bottom row border for given cell size and number of rows and columns
    print(row_col*("+" + "-"*cell_size) + "+") # prints bottom +- row border
