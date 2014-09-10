# Deselect

## Overview

A simple Sublime Text 3 plugin that adds a hotkey to deselect all selected text; based on a [forum post](https://www.sublimetext.com/forum/viewtopic.php?f=2&t=4716#p21219) by [Liam Cain](https://github.com/BoundInCode/).

## Usage

The hotkey defaults to <kbd>Esc</kbd>. Use the `deselect` command in your key bindings to customize it, e.g.:


```json
[
  { "keys": ["escape"], "command": "deselect", "context":
      [
          { "key": "selection_empty", "operator": "equal", "operand": false, "match_all": true }
      ]   
  }
]
```

Please make sure to include the `context` in your custom key binding as it might otherwise interfere with other Sublime functions.

## License

*Copyright 2012 [Liam Cain](https://github.com/BoundInCode/)*

*Copyright 2014 Glutanimate*