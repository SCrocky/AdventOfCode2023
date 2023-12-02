"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look.
The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles.
Two puzzles will be made available on each day in the Advent calendar;
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions")
and hang on did you just say the sky ("of course, where do you think snow comes from")
when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input)
has been amended by a very young Elf who was apparently just excited to show off her art skills.
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text;
each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order)
to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
Consider your entire calibration document. What is the sum of all of the calibration values?


==========> Add your input in the github repo, in the `inputs` folder. Path: `inputs/pb_1_input`
"""


def digit_maker(line: str) -> int:
    """
    Given a str containing at least two digits, returns the concatenation of the first and last as an int.

    :param line: str containing at least 2 digits
    :return: int
    """
    int_line = "".join(filter(str.isdigit, line))
    return int(int_line[0]+int_line[-1])


def calibrate_doc(document: str) -> int:
    """
    Sums up the `digit_maker` results for each line in the document.

    :param document: str, input file from Advent of Code
    :return: int, sum of lines
    """
    with open(document) as reader:
        data = reader.read()

    lines = data.split("\n")
    lines.remove("")

    return sum([digit_maker(line) for line in lines])


# Answer to part 1
print(f"Answer to part 1: {calibrate_doc('inputs/pb_1_input')}")

"""
--- Part Two ---

Your calculation isn't quite right. 
It looks like some of the digits are actually spelled out with letters: 

one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""

STR_INTS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
WORD_INTS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

WORDS_TO_INTS = dict(zip(WORD_INTS, STR_INTS))
WORDS_TO_INTS.update(dict(zip(STR_INTS, STR_INTS)))


def fixed_digit_maker(line: str) -> int:
    """
    Given a str containing at least two digits, returns the concatenation of the first and last as an int.
    Digits can be written as words as well.

    :param line: str containing at least 2 digits
    :return: int
    """
    first = {"pos": float("inf"), "value": None}
    last = {"pos": -1, "value": None}
    for digit in STR_INTS + WORD_INTS:
        found_pos = line.find(digit)
        if found_pos != -1 and found_pos < first["pos"]:
            first = {"pos": found_pos, "value": WORDS_TO_INTS[digit]}
        found_pos = line.rfind(digit)
        if found_pos > last["pos"]:
            last = {"pos": found_pos, "value": WORDS_TO_INTS[digit]}

    return int(first["value"] + last["value"])


def recalibrate_doc(document: str) -> int:
    """
    Sums up the `digit_maker` results for each line in the document.

    :param document: str, input file from Advent of Code
    :return: int, sum of lines
    """
    with open(document) as reader:
        data = reader.read()

    lines = data.split("\n")
    lines.remove("")

    return sum([fixed_digit_maker(line) for line in lines])


# Answer to part 2
print(f"Answer to part 1: {recalibrate_doc('inputs/pb_1_input')}")

