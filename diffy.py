import sys
import diff_match_patch as dmp_module
from colorama import init, Fore, Style

init()

a = sys.argv[-2]
b = sys.argv[-1]

differ = dmp_module.diff_match_patch()
diffs = differ.diff_main(a, b)
differ.diff_cleanupSemantic(diffs)

top_line = ""
bottom_line = ""
i = 0
while i < len(diffs):
  pair = diffs[i]
  if pair[0] == differ.DIFF_EQUAL:
    top_line += Style.RESET_ALL + pair[1]
    bottom_line += Style.RESET_ALL + pair[1]

  elif pair[0] == differ.DIFF_DELETE:
    if i + 1 < len(diffs) and diffs[i + 1][0] != differ.DIFF_INSERT:
      top_line += Style.BRIGHT + Fore.RED + pair[1]
      bottom_line += Style.RESET_ALL + (" " * len(pair[1]))
    elif i + 1 == len(diffs):
      top_line += Style.BRIGHT + Fore.RED + pair[1]
    else:
      top_line += Style.BRIGHT + Fore.YELLOW + pair[1]

  elif pair[0] == differ.DIFF_INSERT:
    if i - 1 < 0 or diffs[i - 1][0] == differ.DIFF_EQUAL:
      bottom_line += Style.BRIGHT + Fore.GREEN + pair[1]
      top_line += Style.RESET_ALL + (" " * len(pair[1]))
    else:
      bottom_line += Style.BRIGHT + Fore.YELLOW + pair[1]

  i += 1

print top_line
print bottom_line
