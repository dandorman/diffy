#! /Volumes/HDD/ddorman/.virtualenv/diffy/bin/python
import sys
import diff_match_patch as dmp_module
from colorama import init, Fore, Style

init()

class Diffy(object):

  def __init__(self):
    self.differ = dmp_module.diff_match_patch()
    self.diff_output = []

  def diff(self, a, b):
    diffs = self.differ.diff_main(a, b)

    top_line, bottom_line = "", ""
    for position, (action, text) in enumerate(diffs):
      if action == self.differ.DIFF_EQUAL:
        top_line += text
        bottom_line += text

      elif action == self.differ.DIFF_DELETE:
        next_action, next_text = position + 1 < len(diffs) and diffs[position + 1] or (None, None)

        if next_action != self.differ.DIFF_INSERT:
          top_line += self.engorge(text)
          bottom_line += " " * len(text)
        elif not next_action:
          top_line += self.engorge(text)
        else:
          top_line += self.jaundice(text.center(max(len(next_text), len(text))))

      elif action == self.differ.DIFF_INSERT:
        previous_action, previous_text = position - 1 >= 0 and diffs[position - 1] or (None, None)

        if previous_action == self.differ.DIFF_EQUAL:
          bottom_line += self.putrefy(text)
          top_line += " " * len(text)
        else:
          bottom_line += self.jaundice(text.center(max(len(previous_text), len(text))))

    self.diff_output = [top_line, bottom_line]
    return self

  def colorize(self, color, text):
    return Style.BRIGHT + color + text + Style.RESET_ALL

  def engorge(self, text):
    return self.colorize(Fore.RED, text)

  def jaundice(self, text):
    return self.colorize(Fore.YELLOW, text)

  def putrefy(self, text):
    return self.colorize(Fore.GREEN, text)

  def display(self):
    print "\n".join(self.diff_output)

if __name__ == "__main__":
  if len(sys.argv) == 3:
    a = sys.argv[-2]
    b = sys.argv[-1]

    Diffy().diff(a, b).display()
  else:
    print "USAGE: diffy [a string] [another string]"
