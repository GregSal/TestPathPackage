# VS Code TODO HighlightSettings

## better-comments
```json
  "better-comments.tags": [
    {
      "tag": "!",
      "color": "#98C379",
      "strikethrough": false,
      "backgroundColor": "transparent"
    },
    {
      "tag": "?",
      "color": "#FF8C00",
      "strikethrough": false,
      "backgroundColor": "transparent"
    },
    {
      "tag": "//",
      "color": "#3498DB",
      "strikethrough": true,
      "backgroundColor": "transparent"
    },
    {
      "tag": "xx",
      "color": "#FF2D00",
      "strikethrough": true,
      "backgroundColor": "transparent"
    },
    {
      "tag": "*",
      "color": "#FF8C00",
      "strikethrough": false,
      "backgroundColor": "transparent"
    }
  ],
  "better-comments.highlightPlainText": true,
```

## todo-tree
```json
    "todo-tree.highlights.enabled": false,
    "todo-tree.highlights.customHighlight": {
      "Question": {
        "icon": "question",
        "iconColour": "red",
        "background ": "black",
        "type": "text"
      },
      "TODO": {
        "icon": "check",
        "type": "text"
      },
      "FIXME": {
        "icon": "alert",
        "foreground": "black",
        "iconColour": "yellow",
        "type": "line"
      },
      "Done To Here": {
        "icon": "arrow-right",
        "iconColour": "#50FF00",
        "type": "tag"
      }
  },
  "todo-tree.highlights.defaultHighlight": {
    "icon": "alert",
    "type": "text",
    "foreground": "red",
    "background": "white",
    "opacity": 50,
    "iconColour": "blue"
    },
    "todo-tree.regex.regexCaseSensitive": false,
    "todo-tree.tree.showCountsInTree": true,
    "todo-tree.general.statusBar": "tags",
    "todo-tree.general.tags": [
      "TODO",
      "FIXME",
      "Question",
      "Done To Here"
    ],
```

## todohighlight
```json
    "todohighlight.isCaseSensitive": true,
    "todohighlight.isEnable": true,
    "todohighlight.keywords": [
      "DEBUG:",
      "REVIEW:",
      {
        "text": "NOTE",
        "color": "#ff0000",
        "backgroundColor": "yellow",
        "overviewRulerColor": "grey"
      },
      {
        "text": "Question",
        "color": "#000",
        "backgroundColor": "cyan",
        "isWholeLine": false
      },
      {
        "text": "FIXME",
        "color": "red",
        "border": "1px solid red",
        "borderRadius": "2px",
        //NOTE: using borderRadius along with `border` or you will see nothing change
        "backgroundColor": "rgba(0,0,0,.2)"
        //other styling properties goes here ...
      },
      {
        "text": "TODO",
        "color": "#ff0000",
        "backgroundColor": "#87CEFA",
        "overviewRulerColor": "yellow"
      },
      {
        "text": "Done To Here",
        "color": "#000",
        "backgroundColor": "#00FF00",
        "overviewRulerColor": "yellow",
        "fontWeight": "bold"
      },
    ],
    "todohighlight.include": [
      "**/*.js",
      "**/*.jsx",
      "**/*.py",
      "**/*.xml",
      "**/*.html",
      "**/*.css",
      "**/*.scss"
    ],
    "todohighlight.exclude": [
      "**/node_modules/**",
      "**/bower_components/**",
      "**/dist/**",
      "**/build/**",
      "**/.vscode/**",
      "**/.github/**",
      "**/_output/**",
      "**/*.min.*",
      "**/*.map",
      "**/.next/**"
    ],
```