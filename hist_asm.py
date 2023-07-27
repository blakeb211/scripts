#!/usr/bin/env python3

"""
script to print ascii histogram of assembly instructions from objdump -d
"""

def extract_columns(filename, start_col, end_col):
    with open(filename, 'r') as file:
        for line in file:
            if len(line) >= 9 and line[8] == ':':
                yield line[start_col - 1:end_col]

def count_instructions(filename, start_col, end_col):
    instructions = {}
    for column_text in extract_columns(filename, start_col, end_col):
        # Only include lines that have assembly instruction
        instructions[column_text] = instructions.get(column_text, 0) + 1
    return instructions

def draw_ascii_histogram(instructions):
    max_count = max(instructions.values())
    histogram_width = 50  # Adjust this value to change the width of the histogram

    print("ASCII Histogram:")
    for char, count in instructions.items():
        scaled_count = int(count * histogram_width / max_count)
        histogram_bar = '#' * scaled_count
        print(f"{char}: {histogram_bar}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("USAGE: <script name> objdump_output.asm")
        exit(0);
    filename = sys.argv[1]
    start_col = 33
    end_col = 39

    instructions = count_instructions(filename, start_col, end_col)
    draw_ascii_histogram(instructions)

