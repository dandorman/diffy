#! /Volumes/HDD/.virtualenv/diffy/bin/python
import sys
import diff_match_patch as dmp_module
from colorama import init, Fore, Style

init()

class Diffy(object):

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def diff(self):
    differ = dmp_module.diff_match_patch()
    diffs = differ.diff_main(self.a, self.b)
    differ.diff_cleanupSemantic(diffs)

    top_line, bottom_line = "", ""
    for position, (action, text) in enumerate(diffs):

      if action == differ.DIFF_EQUAL:
        top_line += text
        bottom_line += text

      elif action == differ.DIFF_DELETE:
        if position + 1 < len(diffs) and diffs[position + 1][0] != differ.DIFF_INSERT:
          top_line += self.engorge(text)
          bottom_line += " " * len(text)
        elif position + 1 == len(diffs):
          top_line += self.engorge(text)
        else:
          top_line += self.jaundice(text)

      elif action == differ.DIFF_INSERT:
        if position - 1 < 0 or diffs[position - 1][0] == differ.DIFF_EQUAL:
          bottom_line += self.putrefy(text)
          top_line += " " * len(text)
        else:
          bottom_line += self.jaundice(text)

    return [top_line, bottom_line]

  def colorize(self, color, text):
    return Style.BRIGHT + color + text + Style.RESET_ALL

  def engorge(self, text):
    return self.colorize(Fore.RED, text)

  def jaundice(self, text):
    return self.colorize(Fore.YELLOW, text)

  def putrefy(self, text):
    return self.colorize(Fore.GREEN, text)

  def output(self):
    return "\n".join(self.diff())

if __name__ == "__main__":
  a = sys.argv[-2]
  b = sys.argv[-1]

  print Diffy(a, b).output()
